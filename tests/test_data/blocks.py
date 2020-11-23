"""
example DataBlocks of each type
"""
import numpy as np

from peepingtom.core import PointBlock, LineBlock, OrientationBlock, ImageBlock, PropertyBlock, ParticleBlock
from peepingtom.utils.helpers import linalg_helper

# points
n = 100

x = np.random.normal(0, 10, n)
y = np.random.normal(0, 10, n)
v = np.random.normal(0, 50, n)

xyz = np.column_stack([x, y, v])

pointblock = PointBlock(xyz)

# line
v = np.linspace(0.5, 5 * np.pi, n)
x = np.sin(v)
y = np.cos(v)

xyz = np.column_stack([x, y, v])

lineblock = LineBlock(xyz)

# orientations
n = 100
v = np.linspace(0.5, 2 * np.pi, n)
x = np.sin(v)
y = np.cos(v)
z = np.zeros(n)

xyz = np.column_stack([x, y, z])
unit_z = np.asarray([0, 0, 1])
rotation_matrices = linalg_helper.align_vectors(unit_z, xyz)

orientationblock = OrientationBlock(rotation_matrices)

# properties
n = 100
p_dict = {'p1': np.ones((n))}

propertyblock = PropertyBlock(p_dict)

# particles
particleblock = ParticleBlock(pointblock, orientationblock, propertyblock)

# image
img = np.ones((10, 10, 10))
imageblock = ImageBlock(img)
