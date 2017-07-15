import math


class Vector3D:

    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return "(%f, %f, %f)" % (self.x, self.y, self.z)

    def scale(self, magnitude):
        return Vector3D(self.x * magnitude, self.y * magnitude, self.z * magnitude)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def add(self, vec):
        return Vector3D(self.x + vec.x, self.y + vec.y, self.z + vec.z)

    def subtract(self, vec):
        return self.add(vec.scale(-1))

    def translate(self, vec):
        self.x += vec.x
        self.y += vec.y
        self.z += vec.z

    def relative_to(self, vec):
        return self.subtract(vec)

    def transform(self, matrix):
        # x, y, z = [sum(components) for components in ]
        # TODO: make this more efficient!
        return Vector3D(
            self.x * matrix.values[0][0] + self.y * matrix.values[0][1] + self.z * matrix.values[0][2],
            self.x * matrix.values[1][0] + self.y * matrix.values[1][1] + self.z * matrix.values[1][2],
            self.x * matrix.values[2][0] + self.y * matrix.values[2][1] + self.z * matrix.values[2][2]
        )


class Matrix3D:

    def __init__(self, values):
        # self.values = [x for x in [y for y in values]]
        self.values = values


class Rotation3D(Matrix3D):

    X_AXIS = 0
    Y_AXIS = 1
    Z_AXIS = 2

    def __init__(self, angle, axis):
        if axis == Rotation3D.X_AXIS:
            Matrix3D.__init__(self, [
                    [1,               0,                0],
                    [0, math.cos(angle), -math.sin(angle)],
                    [0, math.sin(angle), math.cos(angle)]
                ])
        elif axis == Rotation3D.Y_AXIS:
            Matrix3D.__init__(self, [
                    [math.cos(angle),  0, math.sin(angle)],
                    [0,                1,               0],
                    [-math.sin(angle), 0, math.cos(angle)]
                ])
        elif axis == Rotation3D.Z_AXIS:
            Matrix3D.__init__(self, [
                    [math.cos(angle), -math.sin(angle), 0],
                    [math.sin(angle),  math.cos(angle), 0],
                    [              0,                0, 1]
                ])


def convert_to_components(magnitude, angle_horizontal, angle_vertical):
    x = magnitude * math.sin(angle_horizontal) * math.cos(angle_vertical)
    y = -1 * magnitude * math.sin(angle_vertical)
    z = magnitude * math.cos(angle_horizontal) * math.cos(angle_vertical)
    return Vector3D(x, y, z)


def dot_product(vecA, vecB):
    return vecA.x * vecB.x + vecA.y * vecB.y + vecA.z * vecB.z


def cross_product(vecA, vecB):
    x = vecA.y * vecB.z - vecA.z * vecB.y
    y = -1 * (vecA.x * vecB.z - vecA.z * vecB.x)
    z = vecA.x * vecB.y - vecA.y * vecB.x
    return Vector3D(x, y, z)


X_UNIT_VECTOR = Vector3D(1, 0, 0)
Y_UNIT_VECTOR = Vector3D(0, 1, 0)
Z_UNIT_VECTOR = Vector3D(0, 0, 1)