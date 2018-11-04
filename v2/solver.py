# Implementation of the solver
import cube as c
import agent as a

# Get a new agent and a new cube
cube = c.Cube()
agent = a.Agent(cube)

# Start
TRAIN_CASES = 1000

TEST_CASES = 1000

for case in range(TEST_CASES):
    # Scramble the cube
