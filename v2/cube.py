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
      # Rotate the face itself clockwise
      self.front = self.rotate_face(self.front)
      # Perform the rotations on the edges
      # The top and bottom edges can save values before transfer
      new_top = [self.left[row][-1] for row in reversed(range(self.size))]
      new_bottom = [self.right[row][0] for row in range(self.size)]
      # Transfer top and bottom to the sides
      # Top to right
      for idx in range(self.size):
         self.right[idx][0] = self.top[-1][idx]

      # Bottom to left
      for idx in range(self.size):
         self.left[idx][-1] = self.bottom[0][idx]
      
      # Replace the top and bottom
      self.top[-1] = new_top
      self.bottom[0] = new_bottom
      

   def rotate_back(self):
      """
      Rotate back face of the cube
      """
      # Rotate the face itself clockwise
      self.back = self.rotate_face(self.back)

   def rotate_left(self):
      """
      Rotate left face of the cube
      """
      # Rotate the face itself clockwise
      self.left = self.rotate_face(self.left)

   def rotate_right(self):
      """
      Rotate right side clockwise
      """
      # Rotate the face itself clockwise  
      self.right = self.rotate_face(self.right)

   def rotate_top(self):
      """
      Rotate top clockwise
      """
      # Rotate the face itself clockwisez 
      self.top = self.rotate_face(self.top)

   def rotate_bottom(self):
      """
      Rotate bottom face clockwise
      """
      # Rotate the face itself clockwise
      self.bottom = self.rotate_face(self.bottom)

   def get_size(self):
   	"""
		Returns the n dimension of the cube
		"""
   	return self.size
