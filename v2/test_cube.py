# Import testing

import pytest
import cube
import unittest
from unittest.mock import MagicMock

def test_cube_size():
   c = cube.Cube()
   assert c.get_size() == 3

def test_rotate_bottom():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.bottom)
    c.rotate_bottom()
    assert c.front == [[0,0,0],[0,0,0],[1,1,1]]
