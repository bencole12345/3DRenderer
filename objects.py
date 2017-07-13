class Cube:

    def __init__(self, centre, size):
        x, y, z = centre
        halfsize = size / 2
        self.vertices = [[_x, _y, _z] for _x in (x-halfsize, x+halfsize) for _y in (y-halfsize, y+halfsize) for _z in (z-halfsize, z+halfsize)]
        self.edges = [[n, n+4] for n in range(4)] + [[n, n+2] for n in (0, 1, 4, 5)] + [[2*n, 2*n+1] for n in range(4)]
