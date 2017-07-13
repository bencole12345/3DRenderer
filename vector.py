import math


class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

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