import errno
import os

from .. import gen

class Build:
    def __init__(self):
        self.gendir = 'build.ninja.generated'
        self.cases = []

    def add(self, case):
        self.cases.append(case)

    def write(self):
        with open('build.ninja', 'wt') as out:
            g = gen.Generator(out)
            g.header()

            g.w.variable('builddir', 'build')
            g.w.variable('gendir', self.gendir)

            g.w.rule('generate', command='./generate.py', generator=True)
            g.w.build('build.ninja', 'generate', implicit='generate.py')

            g.w.include('build.properties')
            g.w.include('ninja/rules.ninja')

            for case in self.cases:
                g.w.include('$gendir/{case}.build.ninja'.format(case=case))

        try:
            os.makedirs(self.gendir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

        for case in self.cases:
            case.write(self)

