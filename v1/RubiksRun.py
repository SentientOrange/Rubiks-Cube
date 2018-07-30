'''RunApp.py

This program imports Grid.py and MDP.py and runs certain algorithms to
demonstrate aspects of reinforcement learning.

'''

import Cubes, MDP

## Q Value Iteration -- displays the Q value iteration method for rubiks cube
def Rubik_QValues_string(Q_dict):
    # IMPLEMENT THIS
    for row in range(0, 3):
        unit_string = ""
        for col in range(0, 4):
            if not (col == 1 and row == 1):
                unit_string += "["
                # Find the best Q for this one along with the action used
                best_action = None
                best_q = None
                for action in Grid.ACTIONS:
                    if best_action == None:
                        best_action = action
                        best_q = Q_dict[((col,row),action)][0]
                    else:
                        if (((col,row),action) in Q_dict):
                            if Q_dict[((col,row),action)][0] > best_q:
                                best_action = action
                                best_q = Q_dict[((col,row),action)][0]
                        else:
                            best_action = "None"
                            best_q = "0"
                unit_string += str(best_action) + ": " + str(best_q) + "]"
            else:
                unit_string += "None ]"
        print(unit_string)
        

def test():
    '''Create the MDP, then run an episode of random actions for 10 steps.'''
    
    # USING RULES FOR 3x3x3
    rubik_MDP = MDP.MDP()
    rubik_MDP.register_start_state(Cubes.START_STATE)
    rubik_MDP.register_actions(Cubes.ActionOps)
    rubik_MDP.register_operators(Cubes.OPERATORS)
    rubik_MDP.register_transition_function(Cubes.T)
    rubik_MDP.register_reward_function(Cubes.threesReward)
    rubik_MDP.register_goal_state(Cubes.GOAL_STATE_THREE)
    rubik_MDP.register_features([Cubes.one_side,Cubes.level1complete, Cubes.crosses_complete, Cubes.corners_complete])
    rubik_MDP.register_weights([7,12,5,5])
    # grid_MDP.random_episode(100)
    rubik_MDP.generateAllStates()
    # Uncomment the following, when you are ready...
    print("=== Q LEARNING ===")
    rubik_MDP.QLearning(0.3, 2, 0.6)
    #print(GW_QValues_string(grid_MDP.Q))
    
test()
