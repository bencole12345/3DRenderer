import math

from vector import *


class Camera:

    def __init__(self, x=0, y=0, z=0):
        self.position = Vector3D(x, y, z)
        self.angle_vertical = 0
        self.angle_horizontal = 0

    def get_camera_vector(self):
        return convert_to_components(1, self.angle_horizontal, self.angle_vertical)

    def move_forwards(self, dist):
        camera_vector = self.get_camera_vector()
        movement_vector = camera_vector.scale(dist)
        self.position.translate(movement_vector)

    def move_backwards(self, dist):
        self.move_forwards(-dist)

    def move_left(self, dist):
        camera_vector = self.get_camera_vector()
        movement_vector = cross_product(camera_vector, Y_UNIT_VECTOR).scale(dist)
        self.position.translate(movement_vector)

    def move_right(self, dist):
        self.move_left(-dist)

    def move_up(self, dist):
        camera_vector = self.get_camera_vector()
        movement_vector = cross_product(cross_product(Y_UNIT_VECTOR, camera_vector), camera_vector).scale(dist)
        self.position.translate(movement_vector)

    def move_down(self, dist):
        self.move_up(-dist)

    def rotate_up(self, angle):
        self.angle_vertical += angle

    def rotate_down(self, angle):
        self.angle_vertical -= angle

    def rotate_left(self, angle):
        self.angle_horizontal -= angle

    def rotate_right(self, angle):
        self.angle_horizontal += angle
