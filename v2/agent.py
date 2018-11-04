# Contains the code base for an agent class that acts on the rubik's cube
import cube as c

class Agent:
   def __init__(self):
      """
      Initialize the Agent using the proper parameters
      The reference to a Rubik's cube must be passed in
      """
      # All actions are performed in a clockwise rotation of one of six sides
      self.actions = ['front', 'back', 'left', 'right', 'top', 'bottom']
      # The memory representaiton of states
      self.q_table = {}

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
         
   def solve(self, cube):
      """
      Utilize some method of solving a rubik's cube and looks to solve it.
      """
      pass
   
   def heuristic(self, cube):
      """
      Heuristic characteristic to this agent
      Takes in a verbose argument. If this is true, we should print out the heuristic evaluations per state was we go
      """
      pass