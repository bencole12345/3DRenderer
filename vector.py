import math


class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def convert_to_components(magnitude, angle_horizontal, angle_vertical):
    x = magnitude * math.sin(angle_horizontal) * math.cos(angle_vertical)
    y = -1 * magnitude * math.sin(angle_vertical)
    z = magnitude * math.cos(angle_horizontal) * math.cos(angle_vertical)


def dot_product(vecA, vecB):
    return vecA.x * vecB.x + vecA.y * vecB.y + vecA.z * vecB.z


def cross_product(vecA, vecB):
    x = vecA.y * vecB.z - vecA.z * vecB.y
    y = -1 * (vecA.x * vecB.z - vecA.z * vecB.x)
    z = vecA.x * vecB.z - vecA.z * vecB.x
    return Vector3D(x, y, z)