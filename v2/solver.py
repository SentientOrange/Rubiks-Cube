# Implementation of the solver
import cube as c
import agent as a
import copy

# Get a new agent
agent = a.Agent()

actions = agent.get_actions()

# Start
TRAIN_CASES = 45

TEST_CASES = 1000

SCRAMBLE_MOVES = 20

MAX_MOVES = 200

EXPLORATION_PERCENTAGE = 15

GAMMA = 0.8 # DISCOUNT FACTOR

ALPHA = 1 # LEARNING RATE

SIZE = 2

base = c.Cube(SIZE)
base.scramble(SCRAMBLE_MOVES)

# Build the q learning table training the agent
for case in range(TRAIN_CASES):
    # Scramble the cube

    cube = copy.deepcopy(base)
    print("Running Training Case:", case)
    print("Cube size:", SIZE)
    print("Training with DISCOUNT FACTOR (GAMMA):", GAMMA, "- LEARNING RATE (ALPHA)", ALPHA, "- EXPLORATION PERCENTAGE", EXPLORATION_PERCENTAGE,"%")

    # The agent should attempt to solve the cube.
    agent.solve(cube, MAX_MOVES, EXPLORATION_PERCENTAGE, GAMMA,alpha=ALPHA, verbose=False)
    print("Agent has seen", len(agent.q_table),"possible states")
    print()

print("Agent trained on",TRAIN_CASES,"training cases")

print()

successes = 0

for case in range(TEST_CASES):
    # Scramble the cube
    print("Test Case ", case)
    cube = c.Cube(SIZE)
    cube.scramble(SCRAMBLE_MOVES)

    # The agent should attempt to solve the cube.
    agent.solve(cube, 20, 5, GAMMA)

    if (cube.is_solved()):
        successes += 1

print("Out of",TEST_CASES,"test cases, the agent solved", successes)