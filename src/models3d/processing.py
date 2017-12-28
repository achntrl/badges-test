from math import sqrt


class Processor(object):
    """This class is doing dummy actions for the exercice purpose. In real life, these actions
    would be costly in resources and would take some time to execute."""

    def __init__(self):
        self.vertices = []

    def configure(self, file):
        with open(file, 'r') as fd:
            for line in fd.readlines():
                vertices = line.rstrip('\n').split(' ')
                self.vertices.append(map(int, vertices))

    def weigh(self):
        weight = 0

        for x, y, z in self.vertices:
            weight = sqrt(x**2 + y**2 + z**2)

        return weight

    def count_vertices(self):
        return len(self.vertices)
