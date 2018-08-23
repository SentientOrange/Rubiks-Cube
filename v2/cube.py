# Derek Wang

# Rubiks Cube Representation

# In order to do this project, we need to define a Rubiks Cube and all provide state management
# An agent should be able to perform any of the different rotations which will allow the agent to solve the cube.

# We will construct this with a 3x3x3 traditional Rubik's Cube in mind but account for variable size

class Cube:
   # Init the cube using a give size
   def __init__(self):
      self.size = 3
      self.front = [[0 for x in range(self.size)] for x in range(self.size)]
      self.left = [[1 for x in range(self.size)] for x in range(self.size)]
      self.back = [[2 for x in range(self.size)] for x in range(self.size)]
      self.top = [[3 for x in range(self.size)] for x in range(self.size)]
      self.right = [[4 for x in range(self.size)] for x in range(self.size)]
      self.bottom = [[5 for x in range(self.size)] for x in range(self.size)]

   def rotate_face(self, matrix):
      """
      Takes in the 2 dimentional face representation and performs the matrix operation of clockwise rotation
      The new matrix is returned
      """
      temp = [[],[],[]] # Generate the new matrix
      for x in reversed(range(self.size)):
         for y in range(self.size):
            temp[y].append(matrix[x][y])
      return temp

   def rotate_front(self):
      """
      Rotate front face of the cube
      """
      pass

   def rotate_back(self):
      """
      Rotate back face of the cube
      """
      pass

   def rotate_left(self):
      """
      Rotate left face of the cube
      """
      pass

   def rotate_right(self):
      """
      Rotate right side clockwise
      """
      pass

   def rotate_top(self):
      """
      Rotate top clockwise
      """
      pass

   def rotate_bottom(self):
      """
      Rotate bottom face clockwise
      """
      pass