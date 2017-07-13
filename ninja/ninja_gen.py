import argparse
import datetime
import ninja_syntax
import os
import sys

class Paths:
    polyMesh = [os.path.join("constant", "polyMesh", f) for f in ["points", "faces", "owner", "neighbour", "boundary"]]

class Case:
    def __init__(self, root):
        self.root = root
        self.blockMeshDict = self.path("system", "blockMeshDict")
        self.controlDict = self.path("system", "controlDict")
        self.decomposeParDict = self.path("system", "decomposeParDict")
        self.extrudeMeshDict = self.path("system", "extrudeMeshDict")
        self.fvSchemes = self.path("system", "fvSchemes")
        self.fvSolution = self.path("system", "fvSolution")
        self.mountainDict = self.path("system", "mountainDict")
        self.T_init = self.path("constant", "T_init")
        self.tracerFieldDict = self.path("system", "tracerFieldDict")
        self.velocityFieldDict = self.path("system", "velocityFieldDict")

        self.polyMesh = [self.path(f) for f in Paths.polyMesh]
        self.systemFiles = [self.fvSchemes, self.fvSolution, self.controlDict]

    def path(self, path, *paths):
        return os.path.join(self.root, path, *paths)

    def __str__(self):
        return self.root

class Generator:
    def __init__(self):
        self.n = ninja_syntax.Writer(sys.stdout)

    def header(self):
        self.n.comment("Generated by \"{}\"".format(" ".join(sys.argv)))
        self.n.comment("at {}".format(datetime.datetime.utcnow().isoformat()))
        self.n.newline()

    def copy(self, source, target):
        self.n.build(outputs=str(target), rule="cp", inputs=str(source))

    def copyAll(self, files, source, target):
        for f in files:
            self.copy(os.path.join(str(source), f), os.path.join(str(target), f))

    def controlDict(self, case, endTime, timestep, writeInterval):
        self.n.build(
                outputs=case.controlDict,
                rule="gen-controlDict",
                inputs=os.path.join("src", "controlDict.template"),
                variables={
                    "endTime": endTime,
                    "timestep": timestep,
                    "writeInterval": writeInterval,
                }
        )
        self.n.newline()

    def s3upload(self, case, implicit=[]):
        implicit += case.polyMesh + case.systemFiles
        self.n.build(
                outputs=case.path("s3.uploaded"),
                rule="s3-upload",
                implicit=implicit,
                variables={"source": case}
        )
        self.n.newline()


class Solver:
    def __init__(self, generator, case, parallel=False, decomposeParDict=None):
        self.g = generator
        self.case = case
        self.parallel = parallel
        self.decomposeParDict = decomposeParDict

    def solve(self, outputs, rule, inputs=None, implicit=[], order_only=None,
              variables={}, implicit_outputs=None):
        implicit += self.case.polyMesh + self.case.systemFiles
        if self.parallel:
            implicit += [self.case.decomposeParDict]

        variables["case"] = self.case
        variables["pool"] = "console"

        self.g.n.build(outputs, rule, inputs, implicit, order_only, 
                variables, implicit_outputs)
        self.g.n.newline() 

        if self.parallel:
            self.g.n.build(
                    outputs=self.case.decomposeParDict,
                    rule="gen-decomposeParDict",
                    inputs=self.decomposeParDict
            )
            self.g.n.newline() 

class Parser:
    def __init__(self):
        self.p = argparse.ArgumentParser()

    def case(self, help="OpenFOAM case directory"):
        self.p.add_argument('case', help=help)

    def meshCase(self):
        self.p.add_argument('meshCase', help="Case directory of the mesh")

    def timestep(self, help="double-precision float"):
        self.p.add_argument('timestep', type=float, help=help)

    def fvSchemes(self):
        self.p.add_argument('fvSchemes', help="OpenFOAM fvSchemes file")

    def solverExecution(self):
        self.p.add_argument('--solver_execution', choices=["serial", "parallel"], default="parallel", help="Determines how the solver is executed [serial]")
