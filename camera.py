import math


class Camera:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.angle_vertical = 0
        self.angle_horizontal = 0

    def move_forwards(self, dist):
        self.x += dist * math.sin(self.angle_horizontal) * math.cos(self.angle_vertical)
        self.y -= dist * math.sin(self.angle_vertical)
        self.z += dist * math.cos(self.angle_horizontal) * math.cos(self.angle_vertical)

    def move_backwards(self, dist):
        self.move_forwards(-dist)

    def move_left(self, dist):
        self.angle_horizontal -= math.pi / 2
        self.move_forwards(dist)
        self.angle_horizontal += math.pi / 2

    def move_right(self, dist):
        self.move_left(-dist)

    def move_up(self, dist):
        self.y -= dist

    def move_down(self, dist):
        self.y += dist

    def rotate_up(self, angle):
        self.angle_vertical += angle

    def rotate_down(self, angle):
        self.angle_vertical -= angle

    def rotate_left(self, angle):
        self.angle_horizontal -= angle

    def rotate_right(self, angle):
        self.angle_horizontal += angle
