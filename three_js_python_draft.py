import numpy as np
from pythreejs import *
from IPython.display import display

# Create a scene
scene = Scene()

# Create a perspective camera
camera = PerspectiveCamera(position=[10, 10, 10], up=[0, 1, 0], children=[DirectionalLight(color='white', position=[3, 5, 1], intensity=0.5)])

# Create a cube geometry
geometry = BoxBufferGeometry(width=2, height=2, depth=2)

# Create a material with a color
material = MeshLambertMaterial(color='purple')

# Create a mesh using the geometry and material
mesh = Mesh(geometry=geometry, material=material)

# Add the mesh to the scene
scene.add(mesh)

# Create a renderer
renderer = Renderer(camera=camera, scene=scene, controls=[OrbitControls(controlling=camera)])

# Display the renderer
display(renderer)
