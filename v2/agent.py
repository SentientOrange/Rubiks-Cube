# Contains the code base for an agent class that acts on the rubik's cube
import cube as c
import copy
import random

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

   def max_q_at_state(self, state):
      """
      Checks the q table for the max q score at the given state using all actions
      """
      max_q = 0
      for action in self.actions:
         key = (state, action)
         if key in self.q_table:
            if self.q_table[key] > max_q:
               max_q = self.q_table[key]

      return max_q

   def get_best_known_move(self, state):
      """
      Get the best move from the given state based on the q table
      """
      max_q = 0
      best_move = 'none'
      for action in self.actions:
         key = (state, action)
         if key in self.q_table:
            if self.q_table[key] > max_q:
               max_q = self.q_table[key]
               best_move = action
      return best_move
         
   def solve(self, cube, threshold=20, optimizer=10, gamma=0.8, alpha=0.1, verbose=False):
      """
      Utilize some method of solving a rubik's cube and looks to solve it.

      Optimizer parameter: lower = more exploration, higher = well trained move selection
      """
      # Optimal solutions show cubes can be solved in less than 20 moves. You can change this value if needed
      iteration = 0

      while not cube.is_solved():

         # Get state representation
         state = self.get_state_rep(cube)
         
         # Select a move
         # We use the optimizer as the percentage of the time we select the optimal move based on the q table

         # Get the best move known
         best_move = self.get_best_known_move(state)

         # Check if the move is none or we need to randomize a move
         if best_move == 'none' or random.randint(1,100) <= optimizer:
            # select random move
            best_move = self.actions[random.randint(0, len(self.actions) - 1)]

         # Get the reward for the best move
         reward = self.reward_heuristic(cube, best_move)

         # Apply the move to the cube
         self.perform_action(best_move, cube)
         next_state = self.get_state_rep(cube)

         # Get the max q score of the next state
         max_next_q = self.max_q_at_state(next_state)
         
         # Update the q_score
         key = (state, best_move)

         # Compute the next q for this state
         old_q = 0
         if key in self.q_table:
            old_q = self.q_table[key]
         q_score = ((1 - alpha) * old_q) + alpha * (reward + (gamma * max_next_q))
         self.q_table[key] = q_score

         if verbose:
            #print("Iteration",iteration,":",key, " found to have a score of ", q_score, "from best move",best_move)
            print("Moves:", iteration, " - states seen",len(self.q_table))

         # By the end of this, the cube should be completed
         # Since this could take a while try limiting loops
         iteration += 1


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
      
      rep = ""

      for face in faces:
         count = 0
         val = face[1][1]
         for x in range(3):
            for y in range(3):
               if face[x][y] == val:
                  count += 1
         rep += str(count)

      return rep

   def reward_heuristic(self, cube, action):
      """
      Evaluate the reward for a state, which is the difference in correct spots between two states squared
      This rewards moves that bring us closer to the max of rewards
      """

      state = self.get_state_rep(cube)
      agg = 0
      for idx in range(len(state)):
         agg += int(state[idx])
      post_cube = copy.deepcopy(cube)
      self.perform_action(action, post_cube)

      # We want to see if this is a goal state and return a high score if it is
      if post_cube.is_solved():
         return 100000

      post_state = self.get_state_rep(post_cube)
      post_agg = 0
      for idx in range(len(post_state)):
         post_agg += int(post_state[idx])

      # We want a high score for goal state
      
      return (agg - post_agg) * (agg - post_agg)
