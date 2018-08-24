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
    assert c.top == [[3,3,3],[3,3,3][3,3,3]]
    assert c.bottom == [[5,5,5],[5,5,5],[5,5,5]]



def test_rotate_top():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.top)
    c.rotate_top()
    assert c.front == [[4,4,4],[0,0,0],[0,0,0]]
    assert c.left == [[0,0,0],[1,1,1],[1,1,1]]
    assert c.back == [[1,1,1],[2,2,2],[2,2,2]]
    assert c.right == [[2,2,2],[4,4,4],[4,4,4]]
    assert c.top == [[3,3,3],[3,3,3][3,3,3]]
    assert c.bottom == [[5,5,5],[5,5,5],[5,5,5]]

def test_rotate_front():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.front)
    c.rotate_top()
    assert c.top == [[3,3,3],[3,3,3][1,1,1]]
    assert c.left == [[1,1,5],[1,1,5],[1,1,5]]
    assert c.bottom == [[4,4,4],[5,5,5],[5,5,5]]
    assert c.right == [[3,4,4],[3,4,4],[3,4,4]]
    assert c.front == [[0,0,0],[0,0,0],[0,0,0]]
    assert c.back == [[2,2,2],[2,2,2],[2,2,2]]

def test_rotate_back():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.back)
    c.rotate_top()
    assert c.top == [[4,4,4],[3,3,3][3,3,3]]
    assert c.left == [[3,1,1],[3,1,1],[3,1,1]]
    assert c.bottom == [[5,5,5],[5,5,5],[1,1,1]]
    assert c.right == [[4,4,5],[4,4,5],[4,4,5]]
    assert c.front == [[0,0,0],[0,0,0],[0,0,0]]
    assert c.back == [[2,2,2],[2,2,2],[2,2,2]]

def test_rotate_right():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.right)
    c.rotate_top()
    assert c.top == [[3,3,0],[3,3,0][3,3,0]]
    assert c.bottom == [[5,5,2],[5,5,2],[5,5,2]]
    assert c.front == [[0,0,5],[0,0,5],[0,0,5]]
    assert c.back == [[3,2,2],[3,2,2],[3,2,2]]
    assert c.left == [[1,1,1],[1,1,1],[1,1,1]]
    assert c.right == [[4,4,4],[4,4,4],[4,4,4]]

def test_rotate_left():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.right)
    c.rotate_top()
    assert c.top == [[2,3,3],[2,3,3][2,3,3]]
    assert c.bottom == [[0,5,5],[0,5,5],[0,5,5]]
    assert c.front == [[3,0,0],[3,0,0],[3,0,0]]
    assert c.back == [[2,2,5],[2,2,5],[2,2,5]]
    assert c.left == [[1,1,1],[1,1,1],[1,1,1]]
    assert c.right == [[4,4,4],[4,4,4],[4,4,4]]
