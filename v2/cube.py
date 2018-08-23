# Derek Wang

# Rubiks Cube Representation

# In order to do this project, we need to define a Rubiks Cube and all provide state management
# An agent should be able to perform any of the different rotations which will allow the agent to solve the cube.

# We will construct this with a 3x3x3 traditional Rubik's Cube in mind but account for variable size
ACTIONS = ['front-face-right',
   'back-face-right',
   'left-face-right',
   'right-face-right',
   'top-face-right',
   'bottom-face-right',
   'front-face-left',
   'back-face-left',
   'left-face-left',
   'right-face-left',
   'top-face-left', 
   'bottom-face-left',
   'end'
]


class Cube:
   # Init the cube using a give size
   def __init__(self, size=3):
      self.size = size
      self.front = [[0 for x in range(size)] for x in range(size)]
      self.left = [[1 for x in range(size)] for x in range(size)]
      self.back = [[2 for x in range(size)] for x in range(size)]
      self.top = [[3 for x in range(size)] for x in range(size)]
      self.right = [[4 for x in range(size)] for x in range(size)]
      self.bottom = [[5 for x in range(size)] for x in range(size)]

