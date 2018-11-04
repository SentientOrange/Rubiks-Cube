# Implementation of the solver
import cube as c
import agent as a

# Get a new agent
agent = a.Agent()

actions = agent.get_actions()

# Start
TRAIN_CASES = 1000

TEST_CASES = 1000

SCRAMBLE_MOVES = 20

# Build the q learning table
for case in range(TEST_CASES):
    # Scramble the cube
    cube = c.Cube()
    cube.scramble(SCRAMBLE_MOVES)
    
