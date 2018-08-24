# This is just a script that runs the cube and does some rotations
# We can use this to see how each rotation works and can use it as a check to make sure that the cube rotates properly

import cube as c
import agent as a

# Cube
cube = c.Cube()

# Agent
agent = a.Agent(cube)

actions = agent.get_actions()

# See initial cube state
print('Initial State')
print()
cube.print_cube()
print()

# Loop through the actions and see what we get
for action in actions:
    # Do a turn and then print the result
    print('Performing', action, 'rotation')
    print()
    agent.perform_action(action)
    cube.print_cube()
    print()

