# Import testing

import pytest
import cube
import unittest
from unittest.mock import MagicMock

def test_cube_size():
   """
   Test the cube size is 3
   """
   c = cube.Cube()
   assert c.get_size() == 3

def test_cube_generation():
   """
   Test that the cube initialized properly 
   """
   c = cube.Cube()
   assert c.get_front() == [[0 for x in range(3)] for y in range(3)]
   assert c.get_left() == [[1 for x in range(3)] for y in range(3)]
   assert c.get_back() == [[2 for x in range(3)] for y in range(3)]
   assert c.get_top() == [[3 for x in range(3)] for y in range(3)]
   assert c.get_right() == [[4 for x in range(3)] for y in range(3)]
   assert c.get_bottom() == [[5 for x in range(3)] for y in range(3)]

def test_cube_frontrotation():
   """
   Test that the cube rotated the front section and corresponding edges correctly
   """
   pass

def test_rotate_face():
   """
   Test the method that we are using to rotate any face
   """
   c = cube.Cube()
   init = [[1,2,7],[2,3,1],[2,3,9]]
   clockwise_rotation = [[2,2,1],[3,3,2],[9,1,7]]
   assert c.rotate_face(init) == clockwise_rotation

def test_rotate_front_basic():
   """
   Test the front rotation method
   """
   c = cube.Cube()
   # Perform the turn
   c.rotate_front()
   # The front face on initialization rotation should be the same
   assert c.get_front() == [[0 for x in range(3)] for y in range(3)]

   # Assert the edges for the edges are correct
   # Test
   for idx in range(3):
      assert c.get_left()[idx][-1] == 5
      assert c.get_top()[-1][idx] == 1
      assert c.get_bottom()[0][idx] == 4
      assert c.get_right()[idx][0] == 3
   
def test_rotate_back_basic():
   """
   Test the front rotation method
   """
   c = cube.Cube()
   # Perform the turn
   c.rotate_back()
   # The front face on initialization rotation should be the same
   assert c.get_back() == [[2 for x in range(3)] for y in range(3)]

   # Assert the edges for the edges are correct
   # Test
   for idx in range(3):
      assert c.get_left()[idx][0] == 3
      assert c.get_top()[0][idx] == 4
      assert c.get_bottom()[-1][idx] == 1
      assert c.get_right()[idx][-1] == 5

def test_rotate_bottom():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.get_bottom())
    c.rotate_bottom()
    assert c.get_front() == [[0,0,0],[0,0,0],[1,1,1]]
    assert c.get_left() == [[1,1,1],[1,1,1],[2,2,2]]
    assert c.get_back() == [[2,2,2],[2,2,2],[4,4,4]]
    assert c.get_right() == [[4,4,4],[4,4,4],[0,0,0]]
    assert c.get_top() == [[3,3,3],[3,3,3],[3,3,3]]
    assert c.get_bottom() == [[5,5,5],[5,5,5],[5,5,5]]

def test_rotate_top():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.get_top())
    c.rotate_top()
    assert c.get_front() == [[4,4,4],[0,0,0],[0,0,0]]
    assert c.get_left() == [[0,0,0],[1,1,1],[1,1,1]]
    assert c.get_back() == [[1,1,1],[2,2,2],[2,2,2]]
    assert c.get_right() == [[2,2,2],[4,4,4],[4,4,4]]
    assert c.get_top() == [[3,3,3],[3,3,3],[3,3,3]]
    assert c.get_bottom() == [[5,5,5],[5,5,5],[5,5,5]]

def test_rotate_front():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.get_front())
    c.rotate_front()
    assert c.get_top() == [[3,3,3],[3,3,3],[1,1,1]]
    assert c.get_left() == [[1,1,5],[1,1,5],[1,1,5]]
    assert c.get_bottom() == [[4,4,4],[5,5,5],[5,5,5]]
    assert c.get_right() == [[3,4,4],[3,4,4],[3,4,4]]
    assert c.get_front() == [[0,0,0],[0,0,0],[0,0,0]]
    assert c.get_back() == [[2,2,2],[2,2,2],[2,2,2]]

def test_rotate_back():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.get_back())
    c.rotate_back()
    assert c.get_top() == [[4,4,4],[3,3,3],[3,3,3]]
    assert c.get_left() == [[3,1,1],[3,1,1],[3,1,1]]
    assert c.get_bottom() == [[5,5,5],[5,5,5],[1,1,1]]
    assert c.get_right() == [[4,4,5],[4,4,5],[4,4,5]]
    assert c.get_front() == [[0,0,0],[0,0,0],[0,0,0]]
    assert c.get_back() == [[2,2,2],[2,2,2],[2,2,2]]

def test_rotate_right():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.get_right())
    c.rotate_right()
    assert c.get_top() == [[3,3,0],[3,3,0],[3,3,0]]
    assert c.get_bottom() == [[5,5,2],[5,5,2],[5,5,2]]
    assert c.get_front() == [[0,0,5],[0,0,5],[0,0,5]]
    assert c.get_back() == [[3,2,2],[3,2,2],[3,2,2]]
    assert c.get_left() == [[1,1,1],[1,1,1],[1,1,1]]
    assert c.get_right() == [[4,4,4],[4,4,4],[4,4,4]]

def test_rotate_left():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.get_left())
    c.rotate_left()
    assert c.get_top() == [[2,3,3],[2,3,3],[2,3,3]]
    assert c.get_bottom() == [[0,5,5],[0,5,5],[0,5,5]]
    assert c.get_front() == [[3,0,0],[3,0,0],[3,0,0]]
    assert c.get_back() == [[2,2,5],[2,2,5],[2,2,5]]
    assert c.get_left() == [[1,1,1],[1,1,1],[1,1,1]]
    assert c.get_right() == [[4,4,4],[4,4,4],[4,4,4]]

