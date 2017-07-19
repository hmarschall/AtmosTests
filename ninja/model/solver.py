class Solver:
    def __init__(self, name, command, parallel):
        self.name = name
        self.command = command
        self.parallel = parallel

    def write(self, generator):
        g = generator

        description = "{name} $case".format(name=self.name)

        if self.parallel:
            g.w.rule(
                    self.name,
                    'ninja/openfoam-solve.sh $case $solver_parallel_tasks "{command} -parallel"'.format(command=self.command),
                    description=description)
        else:
            g.w.rule(self.name, self.command, description=description)

    def __str__(self):
        return self.name
