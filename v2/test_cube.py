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
    assert c.left == [[1,1,1],[1,1,1],[2,2,2]]
    assert c.back == [[2,2,2],[2,2,2],[4,4,4]]
    assert c.right == [[4,4,4],[4,4,4],[0,0,0]]



def test_rotate_top():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.top)
    c.rotate_top()
    assert c.front == [[4,4,4],[0,0,0],[0,0,0]]
    assert c.left == [[0,0,0],[1,1,1],[1,1,1]]
    assert c.back == [[1,1,1],[2,2,2],[2,2,2]]
    assert c.right == [[2,2,2],[4,4,4],[4,4,4]]

def test_rotate_front():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.front)
    c.rotate_top()
    assert c.front == [[4,4,4],[0,0,0],[0,0,0]]
    assert c.left == [[0,0,0],[1,1,1],[1,1,1]]
    assert c.back == [[1,1,1],[2,2,2],[2,2,2]]
    assert c.right == [[2,2,2],[4,4,4],[4,4,4]]
