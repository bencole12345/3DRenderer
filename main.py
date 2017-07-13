import math
import sys
import pygame

from camera import *
from objects import *


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

CAMERA_MOVE_SPEED = 2
CAMERA_ROTATE_SPEED = math.pi / 4


class Renderer:

    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.cubes = []
        self.cubes.append(Cube((0, 0, 0), 2))
        self.camera = Camera(z=-5)

        self.moving_forwards = False
        self.moving_backwards = False
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.looking_up = False
        self.looking_down = False
        self.looking_left = False
        self.looking_right = False

    def handle_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == ord('w'):
                    self.moving_forwards = True
                elif event.key == ord('s'):
                    self.moving_backwards = True
                elif event.key == ord('a'):
                    self.moving_left = True
                elif event.key == ord('d'):
                    self.moving_right = True
                elif event.key == ord('r'):
                    self.moving_up = True
                elif event.key == ord('f'):
                    self.moving_down = True
                elif event.key == pygame.K_UP:
                    self.looking_up = True
                elif event.key == pygame.K_DOWN:
                    self.looking_down = True
                elif event.key == pygame.K_LEFT:
                    self.looking_left = True
                elif event.key == pygame.K_RIGHT:
                    self.looking_right = True
            elif event.type == pygame.KEYUP:
                if event.key == ord('w'):
                    self.moving_forwards = False
                elif event.key == ord('s'):
                    self.moving_backwards = False
                elif event.key == ord('a'):
                    self.moving_left = False
                elif event.key == ord('d'):
                    self.moving_right = False
                elif event.key == ord('r'):
                    self.moving_up = False
                elif event.key == ord('f'):
                    self.moving_down = False
                elif event.key == pygame.K_UP:
                    self.looking_up = False
                elif event.key == pygame.K_DOWN:
                    self.looking_down = False
                elif event.key == pygame.K_LEFT:
                    self.looking_left = False
                elif event.key == pygame.K_RIGHT:
                    self.looking_right = False

    def update(self):
        self.transform_camera()

    def render(self):
        self.screen.fill(WHITE)

        for cube in self.cubes:
            for vertex in cube.vertices:
                x_screen, y_screen = self.get_onscreen_position(vertex)
                # pygame.draw.circle(self.screen, BLACK, (x_screen, y_screen), 3)
            for edge in cube.edges:
                start = cube.vertices[edge[0]]
                end = cube.vertices[edge[1]]
                x1_screen, y1_screen = self.get_onscreen_position(start)
                x2_screen, y2_screen = self.get_onscreen_position(end)
                pygame.draw.line(self.screen, BLACK, (x1_screen, y1_screen), (x2_screen, y2_screen))

        pygame.display.update()

    def get_onscreen_position(self, coords):
        x, y, z = coords

        # Translate relative to camera
        x_rel = x - self.camera.x
        y_rel = y - self.camera.y
        z_rel = z - self.camera.z

        # Perform horizontal rotation (about y axis)
        original_angle = math.atan(x_rel / z_rel)
        rotation_angle = -self.camera.angle_horizontal
        distance = math.sqrt(x_rel**2 + z_rel**2)
        x_rel = distance * math.sin(original_angle + rotation_angle)
        z_rel = distance * math.cos(original_angle + rotation_angle)

        # Perform vertical rotation (about x axis)
        original_angle = math.atan(y_rel / z_rel)
        rotation_angle = -self.camera.angle_vertical
        distance = math.sqrt(z_rel ** 2 + y_rel ** 2)
        y_rel = distance * math.sin(original_angle - rotation_angle)
        z_rel = distance * math.cos(rotation_angle - original_angle)

        # Use relative coordinates to find screen position
        scale = 200 / z_rel
        x_screen = int(WINDOW_WIDTH / 2 + scale * x_rel)
        y_screen = int(WINDOW_HEIGHT / 2 + scale * y_rel)
        return (x_screen, y_screen)

    def transform_camera(self):
        dt = self.clock.get_time() / 1000
        if self.moving_forwards:
            self.camera.move_forwards(CAMERA_MOVE_SPEED * dt)
        if self.moving_backwards:
            self.camera.move_backwards(CAMERA_MOVE_SPEED * dt)
        if self.moving_up:
            self.camera.move_up(CAMERA_MOVE_SPEED * dt)
        if self.moving_down:
            self.camera.move_down(CAMERA_MOVE_SPEED * dt)
        if self.moving_left:
            self.camera.move_left(CAMERA_MOVE_SPEED * dt)
        if self.moving_right:
            self.camera.move_right(CAMERA_MOVE_SPEED * dt)
        if self.looking_up:
            self.camera.rotate_up(CAMERA_ROTATE_SPEED * dt)
        if self.looking_down:
            self.camera.rotate_down(CAMERA_ROTATE_SPEED * dt)
        if self.looking_left:
            self.camera.rotate_left(CAMERA_ROTATE_SPEED * dt)
        if self.looking_right:
            self.camera.rotate_right(CAMERA_ROTATE_SPEED * dt)

    def start(self):
        while True:
            self.handle_inputs()
            self.update()
            self.render()
            self.clock.tick(FPS)


def main():
    pygame.init()
    Renderer().start()


if __name__ == "__main__":
    main()