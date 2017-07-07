'''
Eric Eckert, Derek Wang
eric95, d95wang
Final Project
CSE 415 sp17
Tanimoto

Define a cube

'''

ACTIONS = ['front-face-right', 'back-face-right', 'left-face-right', 'right-face-right', 'top-face-right', 'bottom-face-right',\
    'front-face-left', 'back-face-left', 'left-face-left', 'right-face-left', 'top-face-left', 'bottom-face-left', 'end']
# Note that an action is NOT the same thing as an operator, because
# in an MDP, the action indicates only an intended operator, and
# the actual operator that is used is random, according to the
# probability in the transition table.

class State():
    def __init__(self, d):
        self.d = d

    def __str__(self):
        # Produces a brief textual description of a state.
        d = self.d
        txt = ""
        txt = txt + self.print_face(d[0], "\t   ")
        txt = txt + self.print_four_faces(d[1], d[2], d[4], d[5], "")
        txt = txt + self.print_face(d[3], "\t   ")

        return txt
        
    def print_face(self, face, indent):
        txt = indent
        for row in face:
            for n in row:
                txt = txt+"["+str(n)+"]"
            txt=txt+"\n"+indent
        return txt + "\n"
        
    def print_four_faces(self, face1, face2, face3, face4, indent):
        txt = indent
        for row in range(3):
            for n in face1[row]:
                txt = txt+"["+str(n)+"]"
            txt = txt+"  "
            
            for n in face2[row]:
                txt = txt+"["+str(n)+"]"
            
            txt = txt+"  "
            
            for n in face3[row]:
                txt = txt+"["+str(n)+"]"
                
            txt = txt+"  "
            
            for n in face4[row]:
                txt = txt+"["+str(n)+"]"
            txt=txt+"\n"+indent
            
        return txt + "\n"

    def __eq__(self, s2):
        if not (type(self)==type(s2)): return False
        d1 = self.d; d2 = s2.d
        return d1==d2

    def __hash__(self):
        return (str(self)).__hash__()

    def __copy__(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        news = State([])
        for face in self.d:
            newface = copy_face(face)
            news.d.append(newface)
        
        return news


    def __lt__(self, s2):
        return True

GOAL_STATE_THREE = [[\
            [0,0,0],\
            [0,0,0],\
            [0,0,0]],\
[\
[1,1,1],\
[1,1,1],\
[1,1,1]],\
            [\
            [2,2,2],\
            [2,2,2],\
            [2,2,2]],\
            [\
            [3,3,3],\
            [3,3,3],\
            [3,3,3]],\
                        [\
                        [4,4,4],\
                        [4,4,4],\
                        [4,4,4]],\
            [\
            [5,5,5],\
            [5,5,5],\
            [5,5,5]]\
        ]
        
# Data of a completed 2x2 cube        
GOAL_STATE_TWO = [[\
            [0,0],\
            [0,0]],\
[\
[1,1],\
[1,1]],\
            [\
            [2,2],\
            [2,2]],\
            [\
            [3,3],\
            [3,3]],\
                        [\
                        [4,4],\
                        [4,4]],\
            [\
            [5,5],\
            [5,5]]\
        ]
        

# TODO        
# Define this later when you want to start running a test
INITIAL_STATE = (0,0)
        
# Define the precond - since all moves can be made using a rubiks cube and all of them
# lead to a valid state, this precondition will always be true
def can_move(s):
    return True
    
## ERIC DO THIS
## TODO -- Takes in a state and an action and returns the state following the action     
def move(s, facenum, direction):
    news = s.__copy__()
    
    news.d[facenum] = rotate_face(s, facenum, direction)
    updated_faces = rotate_edge(s, facenum, direction)
    for newf in updated_faces:
        news.d[newf] = updated_faces[newf]
    return news
    
#Rotates the values on a single face (not including the edges)
#0 -> clockwise
#1 -> counter
def rotate_face(s, facenum, direction):
    face = s.d[facenum]
    newf = copy_face(s.d[facenum])
    # if turns == 2:
    #     newf[0] = reversed(face[2])
    #     newf[2] = reversed(face[0])
    #     newf[1] = reversed(face[1])
    
    #Rotate clockwise
    if direction == 1:
        #print("Rotate clockwise")
        for i in range(3):
            for j in range(3):
                newf[i][j] = face[2-j][i]
    #Rotate counterclockwise
    else:
        for i in range(3):
            for j in range(3):
                newf[i][j] = face[j][2-i]
    
    return newf

#looking from the top, the rotated rows will be on the 
def rotate_edge(s, facenum, direction):
    edge_set = edge_rotation[facenum]
    updated_faces = {}
    for i in range(4):
        
        edge_tuple = edge_set[i]
        previous_tuple = edge_set[(i-direction)%4]
        #grab current face we are looking at
        curr_face = s.d[edge_tuple[0]]
        #grab previous face
        prev_face = s.d[previous_tuple[0]]
        #grab edge of previous face
        temp_edge = get_edge(prev_face, previous_tuple[1])
        #update edge of new face
        newf = set_edge(curr_face, edge_tuple[1], temp_edge)
        #Update face
        updated_faces[edge_tuple[0]] = newf
    
    return updated_faces
    
#Maps each face to a tuple. The first element of the tuple is an adjacent face,
#and the second element represents which edge of the adjacent face is to be
#rotated (0-top 1-right 2-bottom 3-left)
#The replacement of edge values is determined by the order of the tuples in the list.
#Each edge represented by a tuple is replaced by the previous one in the list.
edge_rotation = {0:[(1,0),(5,0),(4,0),(2,0)], 1:[(0,3),(2,3),(3,3),(5,1)],\
                2:[(0,2),(4,3),(3,0),(1,1)],3:[(2,2),(4,2),(5,2),(1,2)],\
                4:[(2,1),(0,1),(5,3),(3,1)],5:[(0,0),(1,3),(3,2),(4,1)]}
                
def get_edge(face, edge):
    if edge == 2:
        return face[edge]
    #Bottom edge is reversed because we want the values in clockwise order.
    #on the bottom this means they should be in order from right to left
    elif edge == 0:
        # return reversed(face[edge])
        #print(list(reversed(face[edge])))
        return list(reversed(face[edge]))
    else:
        edge_list = []
        #j is the index within the row. (edge + 1) % 3 means edge 1 -> index 2
        #edge 3 -> index 0
        j = (edge + 1) % 4
        l = range(3)
        if edge == 1:
            l = reversed(l)
        for i in l:
            edge_list.append(face[i][j])
        return edge_list
        
def set_edge(face, edge, new_edge):
    newf = copy_face(face)
    if edge == 2: 
        newf[edge] = new_edge
    elif edge == 0:
        newf[edge] = list(reversed(new_edge))
    else:
        edge_list = []
        #j is the index within the row. (edge + 1) % 3 means edge 1 -> index 2
        #edge 3 -> index 0
        j = (edge + 1) % 4
        l = range(3)
        n = 0
        #Reverse row index if edge = 3
        if edge == 1:
            l = reversed(l)
        for i in l:
            newf[i][j] = new_edge[n]
            n += 1
    
    return newf
    

def copy_face(face):
    newf = []
    for row in face:
        newr = []
        for n in row:
            newr.append(n)
        newf.append(newr)

    return newf

# Define operators
class Operator:

  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)
    
frontFaceRightOp = Operator("Turn the front face to the right",\
                
                   lambda s: can_move(s),\
                   lambda s: move(s, 2,1))

frontFaceLeftOp = Operator("Turn the front face to the left",\
                   lambda s: can_move(s),\
                   lambda s: move(s, 2,-1))

backFaceRightOp = Operator("Turn the back face to the right",\
                   lambda s: can_move(s),\
                   lambda s: move(s, 5,1))

backFaceLeftOp = Operator("Turn the back face to the left",\
                   lambda s: can_move(s),\
                   lambda s: move(s, 5,-1))

leftFaceRightOp = Operator("Turn the left face to the right",\
                   lambda s: can_move(s),\
                   lambda s: move(s, 1,1))

leftFaceLeftOp = Operator("Turn the left face to the left",\
                   lambda s: can_move(s),\
                   lambda s: move(s, 1,-1))

rightFaceRightOp = Operator("Turn the right face to the right",\
                   lambda s: can_move(s),\
                   lambda s: move(s, 4,1))

rightFaceLeftOp = Operator("Turn the right face to the left",\
                   lambda s: can_move(s),\
                   lambda s: move(s, 4,-1))
                   
topFaceRightOp = Operator("Turn the top face to the right",\
                   lambda s: can_move(s),\
                   lambda s: move(s, 0,1))

topFaceLeftOp = Operator("Turn the top face to the left",\
                   lambda s: can_move(s),\
                   lambda s: move(s, 0,-1))

bottomFaceRightOp = Operator("Turn the bottom face to the right",\
                   lambda s: can_move(s),\
                   lambda s: move(s, 3,1))

bottomFaceLeftOp = Operator("Turn the bottom face to the left",\
                   lambda s: can_move(s),\
                   lambda s: move(s, 3, -1))
                   
OPERATORS = [bottomFaceLeftOp, bottomFaceRightOp, topFaceLeftOp, topFaceRightOp, rightFaceLeftOp, rightFaceRightOp,\
             leftFaceLeftOp, leftFaceRightOp, backFaceLeftOp, backFaceRightOp, frontFaceLeftOp, frontFaceRightOp]

# The following dictionary maps each action (except the End action)
# to the three operators that might be randomly chosen to perform it.
# In this MDP, the first gets probability P_normal, and the other two
# each get probability P_noise.


ActionOps = {'bottomFaceLeft': bottomFaceLeftOp,
             'bottomFaceRight': bottomFaceRightOp,
             'topFaceLeft':  topFaceLeftOp,
             'topFaceRight':  topFaceRightOp,
             'rightFaceLeft':  rightFaceLeftOp,
             'rightFaceRight':  rightFaceRightOp,
             'leftFaceLeft':  leftFaceLeftOp,
             'leftFaceRight':  leftFaceRightOp,
             'backFaceLeft':  backFaceLeftOp,
             'backFaceRight':  backFaceRightOp,
             'frontFaceLeft': frontFaceLeftOp,
             'frontFaceRight': frontFaceRightOp
}

P_normal = 0.8   # For use in the transition probability
P_noise  = 0.1


# Transition probability
def T(s, a, sp):
    '''Compute the transition probability for going from state s to
       state sp after taking action a.'''
    for index in range(0, len(ActionOps[a])):
        if ActionOps[a][index].apply(s) == sp:
            if index == 0: return P_normal
            if index == 1: return P_noise            
    return 0.0 # Default case is probability 0.
    

# Reward function
def threesReward(state, action, state_p):
    '''Return the reward associated with transitioning from s to sp via action a.'''
    if state == GOAL_STATE_THREE: return 1.0  # the Goal has been reached
    
    ## If the state is not the goal or is something we haven't seen yet, evaluate using a heuristic (/)
    
    return -0.01   # cost of living.
    
#Returns a list of all complete faces
def level1complete(s):
    #Iterate through all faces
    #complete_faces = []
    complete_faces = 0
    for facenum in range(6):
        face = s.d[facenum]
        #Check if all rows are the same
        if all(face[0] == row for row in face):
            #Check if all elements in single row are the same
            if all(face[0][0] == n for n in face[0]):
                #Check if the edges are complete as well
                if edges_complete(s, facenum):
                    #complete_faces.append(facenum)
                    complete_faces += 1
    return complete_faces
    
#Checks if the edges around a face are complete
def edges_complete(s, facenum):
    #Grab edge set
    edge_set = edge_rotation[facenum]
    for i in range(4):
        
        edge_tuple = edge_set[i]
        #grab current adjacent face we are looking at
        curr_face = s.d[edge_tuple[0]]
        #grab edge of current adjacent face
        temp_edge = get_edge(curr_face, edge_tuple[1])
        #Check if the edge is all equal
        if not all(temp_edge[0] == n for n in temp_edge):
            return False
    
    return True
    
#Checks if there is a cross complete on one side.
# def crosses_complete(s):
#     #cross_faces = []
#     cross_faces = 0
#     for facenum in range(6):
#         face = s.d[facenum]
#         if cross_true(face):
#             cross_correct = True
#             # print("Cross on surface")
#             #Check every edge piece on every edge
#             for edge in range(4):
#                 adjacent_edge_tuple = edge_ajacency[(facenum,edge)]
#                 #Grab the adjacent side face
#                 adjacent_side = s.d[adjacent_edge_tuple[0]]
#                 #Check the center value of adjacent face
#                 adjacent_center = adjacent_side[1][1]
#                 ae = edge_map[adjacent_edge_tuple[1]]
#                 #Grab the adjacent value of the edge piece
#                 adjacent_edge_val = adjacent_side[ae[0]][ae[1]]
#                 #If they're not equal, then the cross is not complete.
#                 if not adjacent_edge_val == adjacent_center:
#                     cross_correct = False
#                     # print("Following edge was not correct: ", edge)
#                     # print("Adj centerL ", adjacent_center)
#                     # print("Adj edge: ", adjacent_edge_val)
#                     #Don't have to check other edges
#                     break
#             #If it was true for every edge, cross is complete
#             #Otherwise check next face.
#             if cross_correct:
#                 #cross_faces.append(facenum)
#                 cross_faces += 1

#     return cross_faces
                
def crosses_complete(s):
    m = 0
    for facenum in range(6):
        face = s.d[facenum]
        facem = 0
        for edge in range(4):
            #Make sure edge piece is same as center
            center = face[1][1]
            edgepiece = face[edge_map[edge][0]][edge_map[edge][1]]
            if not center == edgepiece: continue

            adjacent_edge_tuple = edge_ajacency[(facenum,edge)]
            #Grab the adjacent side face
            adjacent_side = s.d[adjacent_edge_tuple[0]]
            #Check the center value of adjacent face
            adjacent_center = adjacent_side[1][1]
            ae = edge_map[adjacent_edge_tuple[1]]
            #Grab the adjacent value of the edge piece
            adjacent_edge_val = adjacent_side[ae[0]][ae[1]]
            if adjacent_edge_val == adjacent_center: 
                # print("Center: ", center)
                # print("edge: ", edgepiece)
                # print("Adjacent center:", adjacent_center)
                # print("adjacent edge", adjacent_edge_val)
                facem += 1
        if facem > m: m = facem
    return m


def cross_true(face):
    center = face[1][1]
    # for edge_piece in edge_map:
    #     if not center == face[edge_piece[0]][edge_piece[1]]:
    #         return False
    return center == face[0][1] and center == face[2][1] and center == face[1][0] and center == face[1][2]


# def corners_complete(s):
#     #x_faces = []
#     x_faces = 0
#     for facenum in range(6):
#         face = s.d[facenum]
#         if x_true(face):
#             x_correct = True
#             # print("X correct")
#             #Check every edge piece on every edge
#             for edge in range(4):
#                 # print("-------------------")
#                 # print("Edge: ", edge)
#                 adjacent_edge_tuple = edge_ajacency[(facenum,edge)]
#                 #Grab the adjacent side face
#                 adjacent_side = s.d[adjacent_edge_tuple[0]]
#                 #Check the center value of adjacent face
#                 adjacent_center = adjacent_side[1][1]
#                 #print("Adjacent center: ", adjacent_center)
#                 #Grabs 2 corners on the shared edge
#                 ac = corner_map[adjacent_edge_tuple[1]]
#                 #Grab the adjacent value of the edge piece
#                 adjacent_edge_val1 = adjacent_side[ac[0][0]][ac[0][1]]
#                 adjacent_edge_val2 = adjacent_side[ac[1][0]][ac[1][1]]
#                 #print("Adj edge: ", adjacent_edge_val1, " ", adjacent_edge_val2)
#                 #If they're not equal, then the x is not complete.
#                 if not (adjacent_edge_val1 == adjacent_center and adjacent_edge_val2 == adjacent_center):
#                     x_correct = False
#                     #Don't have to check other edges
#                     # print("Following edge was not correct: ", edge)
#                     # print("Adj centerL ", adjacent_center)
#                     # print("Adj edge: ", adjacent_edge_val1, " ", adjacent_edge_val2)
#                     break
#             #If it was true for every edge, x is complete
#             #Otherwise check next face.
#             if x_correct:
#                 #x_faces.append(facenum)
#                 x_faces += 1

#     return x_faces
    
def corners_complete(s):
    #x_faces = []
    m = 0
    for facenum in range(6):
        face = s.d[facenum]
        facem = 0
        for edge in range(4):
            center = face[1][1]
            edgepiece1 = face[corner_map[edge][0][0]][corner_map[edge][0][1]]
            edgepiece2 = face[corner_map[edge][1][0]][corner_map[edge][1][1]]
            if not (center == edgepiece1 and center == edgepiece2): continue
            # print("-------------------")
            # print("Edge: ", edge)
            adjacent_edge_tuple = edge_ajacency[(facenum,edge)]
            #Grab the adjacent side face
            adjacent_side = s.d[adjacent_edge_tuple[0]]
            #Check the center value of adjacent face
            adjacent_center = adjacent_side[1][1]
            #print("Adjacent center: ", adjacent_center)
            #Grabs 2 corners on the shared edge
            ac = corner_map[adjacent_edge_tuple[1]]
            #Grab the adjacent value of the edge piece
            adjacent_edge_val1 = adjacent_side[ac[0][0]][ac[0][1]]
            adjacent_edge_val2 = adjacent_side[ac[1][0]][ac[1][1]]
            #print("Adj edge: ", adjacent_edge_val1, " ", adjacent_edge_val2)
            #If they're not equal, then the x is not complete.
            if (adjacent_edge_val1 == adjacent_center and adjacent_edge_val2 == adjacent_center): facem += 1
        if facem > m: m = facem
    return m
    
def x_true(face):
    center = face[1][1]
    # for edge_piece in edge_map:
    #     if not center == face[edge_piece[0]][edge_piece[1]]:
    #         return False
    return center == face[0][2] and center == face[2][2] and center == face[2][0] and center == face[0][0]

#Returns the greatest number of same elements on the same side
# def one_side(s):
#     m = 0
#     for facenum in range(6):
#         #maxes = {}
#         product = 1
#         face = s.d[facenum]
#         for row in face:
#             for n in row:
#                 #maxes[n] = maxes.get(n,0) + 1
#                 product *=n
#         #facemax = max(maxes.values())
#         #if facemax > m: m = facemax
#         if product > m: m = product
#     return m//100000

def one_side(s):
    m = 0
    for facenum in range(6):

        face = s.d[facenum]
        
        center = face[1][1]
        count = 0
        for row in face:
            for n in row:
                if n == center:
                    count += 1
                #product *=n
        #facemax = max(maxes.values())
        #if facemax > m: m = facemax
        if count > m: m = count
        
    return m

#Features in the form 
#Key: ({map of features to integer values? lists of faces that have features?}, count) -> q value
#features = {({"complete":0,"cross":0,"x":0},0):0.0}

edge_ajacency = {(0,0):(5,0),(0,1):(4,0),(0,2):(2,0),(0,3):(1,0),\
                (1,0):(0,3),(1,1):(2,3),(1,2):(3,3),(1,3):(5,1),\
                (2,0):(0,2),(2,1):(4,3),(2,2):(3,0),(2,3):(1,1),\
                (3,0):(2,2),(3,1):(4,2),(3,2):(5,2),(3,3):(1,2),\
                (4,0):(0,1),(4,1):(5,3),(4,2):(3,1),(4,3):(2,1),\
                (5,0):(0,0),(5,1):(1,3),(5,2):(3,2),(5,3):(4,1)}
                
edge_map = {0:(0,1),1:(1,2),2:(2,1),3:(1,0)}
corner_map = {0:[(0,2),(0,0)],1:[(2,2),(0,2)],2:[(2,2),(2,0)],3:[(0,0),(2,0)]}

test = [[\
            [1,0,1],\
            [0,1,0],\
            [1,0,1]],\
[\
[0,1,0],\
[0,0,1],\
[0,0,0]],\
            [\
            [2,2,2],\
            [2,2,3],\
            [2,2,2]],\
            [\
            [3,3,3],\
            [3,4,3],\
            [3,3,3]],\
                        [\
                        [4,3,4],\
                        [3,4,3],\
                        [4,4,4]],\
            [\
            [5,5,5],\
            [5,5,0],\
            [5,5,5]]\
        ]

# print(ACTIONS)
# print(ActionOps)

# s = State(GOAL_STATE_THREE)
# t = State(test)
# print(s)
# print(corners_complete(s))
# s = move(s, 0, 1)
# print(s)
# print(corners_complete(s))
# s = move(s, 3, 1)
# print(s)
# print(corners_complete(s))
# s = move(s, 2, 1)
# print(s)
# print(corners_complete(s))

# print(t)
# print(corners_complete(t))


t = State(GOAL_STATE_THREE)
t = move(t, 0, 1)
t = move(t, 3, -1)
t = move(t, 2, 1)
t = move(t, 4, -1)
t = move(t, 5, 1)
t = move(t, 0, 1)
t = move(t, 3, -1)
t = move(t, 2, 1)
t = move(t, 4, -1)
t = move(t, 5, 1)
print(t)
START_STATE = t