import pytest
import numpy as np
from numpy.testing import assert_array_equal

from peepingtom.datablocks.simpleblocks.pointblock import PointBlock

# test data pointblock
single_point_2d = [1, 2]
points_2d = [[1, 2], [3, 4]]

single_point_3d = [1, 2, 3]
points_3d = [[1, 2, 3], [4, 5, 6]]

point_nd = np.arange(48).reshape(6, 8)


def test_pointblock_instantiation():
    # test instantiation for 2d, 3d and nd points
    PointBlock(data=single_point_2d)
    PointBlock(data=points_2d)
    PointBlock(data=single_point_3d)
    PointBlock(data=points_3d)


def test_pointblock_xyz():
    # test 'x', 'y' and 'z' properties
    block = PointBlock(data=single_point_2d)
    assert_array_equal(block.x, [[1]])
    assert_array_equal(block.y, [[2]])

    block = PointBlock(data=single_point_3d)
    assert_array_equal(block.x, [[1]])
    assert_array_equal(block.y, [[2]])
    assert_array_equal(block.z, [[3]])


def test_pointblock_get_named_dimensions():
    # test _get_named_dimensions method
    block = PointBlock(data=single_point_3d)

    x = block._get_named_dimensions('x')
    assert isinstance(x, np.ndarray)

    # try with multiple named dims
    xyz = block._get_named_dimensions('xyz')
    assert isinstance(xyz, np.ndarray)
    assert xyz.shape == (1, 3)


def test_pointblock_center_of_mass():
    # test center_of_mass property
    # single point case
    block = PointBlock(data=single_point_3d)
    assert_array_equal(block.center_of_mass, single_point_3d)

    # multi point case
    block = PointBlock(data=points_3d)
    assert_array_equal(block.center_of_mass, [2.5, 3.5, 4.5])


def test_pointblock_distance_to():
    # test distance_to method
    block = PointBlock(data=single_point_3d)

    assert block.distance_to([1, 2, 3]) == 0
    assert block.distance_to([2, 3, 4]) == np.sqrt(3)

    # check for failure
    with pytest.raises(ValueError):
        block.distance_to([1, 2, 3, 4, 5, 6])
