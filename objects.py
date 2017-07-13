from vector import *


class Cube:

    def __init__(self, start, end):
        relative = end.relative_to(start)
        self.vertices = [Vector3D(x, y, z) for x in (start.x, start.x+relative.x) for y in (start.y, start.y+relative.y) for z in (start.z, start.z+relative.z)]
        self.edges = [[n, n+4] for n in range(4)] + [[n, n+2] for n in (0, 1, 4, 5)] + [[2*n, 2*n+1] for n in range(4)]

