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

# Build the q learning table training the agent
for case in range(TRAIN_CASES):
    # Scramble the cube
    cube = c.Cube()
    cube.scramble(SCRAMBLE_MOVES)

    # The agent should attempt to solve the cube.
    agent.solve(cube)

print("Agent trained on",TRAIN_CASES,"training cases")
print()

successes = 0

for case in range(TEST_CASES):
    # Scramble the cube
    cube = c.Cube()
    cube.scramble(SCRAMBLE_MOVES)

    # The agent should attempt to solve the cube.
    agent.solve(cube)

    if (cube.is_solved()):
        successes += 1

print("Out of",TEST_CASES,"test cases, the agent solved", successes)