# 3DRenderer

3DRenderer is a very simple 3D rendering engine written using Python and the Pygame library.

Coordinates within the world are stored using the `Vector3D` class. This allows for complex operations, such as the vector cross product. The world is rendered relative to a `Camera` object.

The rendering process consists of two stages. First, the world is transformed from using world coordinates to using coordinates relative to the camera. Once this stage is complete, the coordinates will be relative to the camera, as if the camera were a 'unit camera' located at `(0, 0, 0)` and pointing in the direction parallel to the z-axis. Then, objects are projected onto the screen, multiplying their `x` and `y` displacements from the centre of the screen by a scale derived by dividing an arbitrary constant, `200`, by their `z` value. The further away an object is, the greater its `z` coordinate will be, so the less its `x` and `y` displacements will be from the centre of the screen.

The world can be populated by using world objects from the `objects` module. Currently, only `Cube` exists. Vertices are defined by using an array of `Vector3D` objects, and edges are defined by using a table of indexes, with each entry being a two dimensional array containing the index of the start and end vertices from the array of vertices.

Written for fun by Ben Cole