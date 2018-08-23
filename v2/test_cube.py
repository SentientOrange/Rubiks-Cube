# Import testing

import pytest
import cube

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
   c =cube.Cube()
   init = [[1,2,7],[2,3,1],[2,3,9]]
   clockwise_rotation = [[2,2,1],[3,3,2],[9,1,7]]
   assert c.rotate_face(init) == clockwise_rotation