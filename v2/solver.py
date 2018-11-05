# Implementation of the solver
import cube as c
import agent as a

# Get a new agent
agent = a.Agent()

actions = agent.get_actions()

# Start
TRAIN_CASES = 1

TEST_CASES = 1000

SCRAMBLE_MOVES = 20

MAX_MOVES = 200

EXPLORATION_PERCENTAGE = 10

GAMMA = 0.8

ALPHA = 0.2

# Build the q learning table training the agent
for case in range(TRAIN_CASES):
    # Scramble the cube
    cube = c.Cube()
    cube.scramble(SCRAMBLE_MOVES)
    print("Running Training Case", case)

    # The agent should attempt to solve the cube.
    agent.solve(cube, MAX_MOVES, EXPLORATION_PERCENTAGE, GAMMA,alpha=ALPHA, verbose=True)
    print("Agent has seen", len(agent.q_table),"possible states")

print("Agent trained on",TRAIN_CASES,"training cases")

print()

successes = 0

for case in range(TEST_CASES):
    # Scramble the cube
    cube = c.Cube()
    cube.scramble(SCRAMBLE_MOVES)

    # The agent should attempt to solve the cube.
    agent.solve(cube, 20, 5, GAMMA)

    if (cube.is_solved()):
        successes += 1

print("Out of",TEST_CASES,"test cases, the agent solved", successes)