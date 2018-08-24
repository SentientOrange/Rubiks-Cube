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
   assert c.front == [[0 for x in range(3)] for y in range(3)]
   assert c.left == [[1 for x in range(3)] for y in range(3)]
   assert c.back == [[2 for x in range(3)] for y in range(3)]
   assert c.top == [[3 for x in range(3)] for y in range(3)]
   assert c.right == [[4 for x in range(3)] for y in range(3)]
   assert c.bottom == [[5 for x in range(3)] for y in range(3)]

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

def test_rotate_front():
   """
   Test the front rotation method
   """
   c = cube.Cube()
   # Perform the turn
   c.rotate_front()
   # The front face on initialization rotation should be the same
   assert c.front == [[0 for x in range(3)] for y in range(3)]

   # Assert the edges for the edges are correct
   # Test
   for idx in range(3):
      assert c.left[idx][-1] == 5
      assert c.top[-1][idx] == 1
      assert c.bottom[0][idx] == 4
      assert c.right[idx][0] == 3
   
def test_rotate_back():
   """
   Test the front rotation method
   """
   c = cube.Cube()
   # Perform the turn
   c.rotate_back()
   # The front face on initialization rotation should be the same
   assert c.back == [[2 for x in range(3)] for y in range(3)]

   # Assert the edges for the edges are correct
   # Test
   for idx in range(3):
      assert c.left[idx][0] == 3
      assert c.top[0][idx] == 4
      assert c.bottom[-1][idx] == 1
      assert c.right[idx][-1] == 5

def test_rotate_bottom():
    c = cube.Cube()
    c.rotate_face = MagicMock(return_value=c.bottom)
    c.rotate_bottom()
    assert c.front == [[0,0,0],[0,0,0],[1,1,1]]
