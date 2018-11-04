# Contains the code base for an agent class that acts on the rubik's cube
import cube as c

class Agent:
   def __init__(self):
      """
      Initialize the Agent using the proper parameters
      The reference to a Rubik's cube must be passed in
      """
      # All actions are performed in a clockwise rotation of one of six sides
      self.actions = ['front', 'back', 'left', 'right', 'top', 'bottom', 'none'] # include no move
      # The memory representaiton of states
      self.q_table = {}

      # Epsilon for greedy function
      self.epsilon = 1

   def get_actions(self):
      """
      Returns the action selection
      """
      return self.actions

   def perform_action(self, action, cube):
      """
      Takes in one of the actions and performs the given move on the cube
      """
      if action == 'front':
         cube.rotate_front()
      elif action == 'back':
         cube.rotate_back()
      elif action == 'left':
         cube.rotate_left()
      elif action == 'right':
         cube.rotate_right()
      elif action == 'top':
         cube.rotate_top()
      elif action == 'bottom':
         cube.rotate_bottom()
         
   def solve(self, cube, threshold=20):
      """
      Utilize some method of solving a rubik's cube and looks to solve it.
      """
      # Optimal solutions show cubes can be solved in less than 20 moves. You can change this value if needed
      for turn in range(threshold):
         # Get state representation
         state = self.get_state_rep(cube)
         # Select the best move from the q table
         

         # Apply the move to the cube

         # By the end of this, the cube should be completed


   def get_state_rep(self, cube):
      """
      Define a state representation
      """
      # In this experiment, we can try using the count of correct units in each face as a state
      # this is 9^6 states which actually isn't that many
      faces = [
         cube.get_front(),
         cube.get_back(),
         cube.get_left(),
         cube.get_right(),
         cube.get_top(),
         cube.get_bottom()
      ]
      
      rep = []

      for face in faces:
         count = 0
         val = face[1][1]
         for x in range(3):
            for y in range(3):
               if face[x][y] == val:
                  count += 1
         rep.append(count)

      return rep

   def reward_heuristic(self, cube, action):
      pass

   def q(self, state, action):
      """
      Generate the q value for the table using the given action and cube
      """
      old_q = self.q_table[(state, action)]
