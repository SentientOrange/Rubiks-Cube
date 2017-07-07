'''MDP.py
Eric Eckert
eric95
Derek Wang
d95wang

Provides representations for Markov Decision Processes.
Specifically Q learning with feature approximation

'''
import random
from queue import PriorityQueue
import itertools

REPORTING = False

class MDP:
    def __init__(self):
        self.known_states = set()
        self.succ = {} # hash of adjacency lists by state.

    def register_start_state(self, start_state):
        self.start_state = start_state
        self.current_state = start_state
        self.known_states.add(start_state)

    def register_actions(self, action_list):
        self.actions = action_list
        
    def register_transition_function(self, transition):
        self.T = transition
        
    def register_reward_function(self, reward):
        self.R = reward

    def register_operators(self, op_list):
        self.ops = op_list
        
    def register_goal_state(self, goal_state):
        self.goal_state = goal_state
        
    ## List of features in order of importance by index
    def register_features(self, features):
        self.features = features
        
    ## Register the weights ordered by importance
    def register_weights(self, weights):
        self.weights = weights

    def state_neighbors(self, state):
        '''Return a list of the successors of state.  First check
           in the hash self.succ for these.  If there is no list for
           this state, then construct and save it.
           And then return the neighbors.'''
        neighbors = self.succ.get(state, False)
        if neighbors==False:
            neighbors = [op.apply(state) for op in self.ops]
            self.succ[state]=neighbors
            #self.known_states.update(neighbors)
        return neighbors

    def generateAllStates(self):
        params = [range(6),range(5),range(5),range(1,9)]
        states = itertools.product(*params)
        #print(list(states))
        #Known state is in 3 tuple form: (complete, crossed, xed)
        self.known_states.update(list(states))
        
    ## Evaluates the given state with the features list populated in the MDP
    ## Assigned Weights accounted for

    def QLearning(self, discount, nEpisodes, epsilon):
        self.generateAllStates()
        acts = self.actions
        Qkeys = itertools.product(self.known_states, self.actions)
        #print(list(Qkeys))
        #print((0,0,0) in self.known_states)
        #print(((0,0,0), )
        # IMPLEMENT THIS
        # CREATE Q VALUE HASH table
        #features = {({"complete":0,"cross":0,"x":0},0):0.0}
        #Q(s,a) is mapped to (Qval, count)
        #Start at 0 for all state action pairs
        self.Q = {k:(0, 0) for k in Qkeys}
        
        for i in range(nEpisodes):
            print("======================")
            print("Episode ", i)
            self.current_state = self.start_state
            previousAction = None
            while not self.current_state == self.goal_state:
                
                # look at current state operators, calculate Q values and then choose a move
                #bestQ_op = None
                bestActionQ = -1000
                bestActions = []
                s = self.current_state
                #for op in self.ops:
                
                print(s)
                
                #Calculate random number
                chance_best_route = random.uniform(0.0,1.0)
                #If it's not epsilon percent, we must find the optimal action
                if chance_best_route > epsilon:
                    #Find all neighboring states by applying every action
                    for action in self.actions:
                        nextstate = acts[action].apply(s)
                        # Calculate Q Value
                        #((complete,crossed,xed),action)
                        #Get key for next state features
                        nextOne_Side = self.features[0](nextstate)
                        nextcompleted = self.features[1](nextstate)
                        nextcrossed = self.features[2](nextstate)
                        nextxed = self.features[3](nextstate)
                        
                        maxnextQ = -1000
                        #Find max Q value in next state for every state-action key
                        for a in self.actions:
                            nextQ = self.Q[((nextcompleted,nextcrossed,nextxed,nextOne_Side),a)][0]
                            if nextQ > maxnextQ: maxnextQ = nextQ
                        
                        #If the Q of this next state was more optimal, update it
                        #As the only best action.
                        if maxnextQ > bestActionQ:
                            bestActions = []
                            bestActions.append(action)
                            bestActionQ = maxnextQ
                        
                        #If it's Q value is equal to the current max Q, then add
                        #as one of the best action
                        elif maxnextQ == bestActionQ:
                            bestActions.append(action)
                    
                    
                    # Add Q value and current features to the table
                    
                #If we didn't choose optimal actions, just add all actions
                #To list
                if not bestActions:
                    bestActions += acts
                    
                #Choose random action
                nextAction = random.choice(bestActions)
                print("Action: ", nextAction)
                # Pick a route 11/12 you get the most Q valued one (optimal)
                # YOu should not be able to take the route opposing the one you just took
                
                #chance_best_route = random.uniform(1.0)
                #nextAction = None
                
                # If you don't get that one, choose a completely random move
                # if chance_best_route > epsilon:
                #     ## Take the best Action
                #     # Use best Q and best Q ops
                #     nextAction = random.choice(bestActions)
                #     self.current_staste = acts[aptimalAction].apply(self.current_state)
                    
                # else:
                #     ## You are using a random operator
                #     nextOp = random.choice(self.ops)
                #     self.current_state = acts[nextOp].apply(self.current_state)
                
                
                # -- AT THIS POINT HTE STATE IS UPDATED
                self.current_state = acts[nextAction].apply(s)
                #Update current Q value
                #Calculate key
                one_side = self.features[0](s)
                completed = self.features[1](s)
                crossed = self.features[2](s)
                xed = self.features[3](s)
                print(completed, " ", crossed, " ",xed, " ",one_side)
                count = self.Q[((completed,crossed,xed,one_side),nextAction)][1] + 1
                q = discount * self.Q[((completed,crossed,xed,one_side),nextAction)][0]
                qp = (q / count) + (self.weights[0] * one_side + self.weights[1] * completed + self. weights[2] * crossed + xed * self.weights[3])
                
                self.Q[((completed,crossed,xed,one_side),nextAction)] = (qp, count)
                
        # Do another episode
        
        ## At this point all episodes are done and we have a Q table based on the features
        
        ## Find the most optimal choice for each feature set
        
    
        
        
        
                    