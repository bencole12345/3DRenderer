import math
import sys
import pygame

from camera import *
from objects import *


WINDOW_WIDTH = 2000
WINDOW_HEIGHT = 1500
RENDER_SIZE = min(WINDOW_WIDTH, WINDOW_HEIGHT) / 2
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

CAMERA_MOVE_SPEED = 2
CAMERA_ROTATE_SPEED = math.pi / 2


class Renderer:

    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("3DRenderer")
        self.clock = pygame.time.Clock()
        self.cubes = []
        self.cubes.append(Cube(Vector3D(-1, -1, -1), Vector3D(1, 1, 1)))
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
            # for vertex in cube.vertices:
            #     x_screen, y_screen = self.get_onscreen_position(vertex)
            #     pygame.draw.circle(self.screen, BLACK, (x_screen, y_screen), 3)
            for edge in cube.edges:
                start = cube.vertices[edge[0]]
                end = cube.vertices[edge[1]]
                start_coords = self.get_onscreen_position(start)
                end_coords = self.get_onscreen_position(end)
                if start_coords is not None and end_coords is not None:
                    pygame.draw.line(self.screen, BLACK, start_coords, end_coords, 2)

        pygame.display.update()

    def get_onscreen_position(self, world_position):
        """Calculates the pixel coordiates to render the given world coordinates.
        
        The algorithm:
            1. Translate so that coordinates are relative to the camera (subtract the camera's position vector)
            2. Rotate about the y axis by -self.camera.angle_horizontal
            3. Rotate about the x axis by -self.camera.angle_horizontal
        """

        # Translate relative to camera.
        x_rel = world_position.x - self.camera.position.x
        y_rel = world_position.y - self.camera.position.y
        z_rel = world_position.z - self.camera.position.z

        # Use a matrix for each rotation.
        angle_vertical = -self.camera.angle_vertical
        angle_horizontal = -self.camera.angle_horizontal
        y_rotation_matrix = Rotation3D(angle_horizontal, Rotation3D.Y_AXIS)
        x_rotation_matrix = Rotation3D(angle_vertical, Rotation3D.X_AXIS)
        world_vector = Vector3D(x_rel, y_rel, z_rel)
        relative_vector = world_vector.transform(y_rotation_matrix).transform(x_rotation_matrix)

        # Don't attempt to render anytning that is behind the camera.
        if relative_vector.z <= 0:
            return None

        # Project the coordinates, relative to the camera's viewpoint, onto the screen.
        scale = RENDER_SIZE / relative_vector.z
        x_screen = int(WINDOW_WIDTH / 2 + scale * relative_vector.x)
        y_screen = int(WINDOW_HEIGHT / 2 + scale * relative_vector.y)
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