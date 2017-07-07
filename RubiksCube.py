'''
Eric Eckert, Derek Wang
eric95, d95wang
Final Project
CSE 415 sp17
Tanimoto
'''

import itertools

#TODO remove can_move, since all Rubik's cube moves are always legal
def can_move(s,facenum, turns):
    return True

def move(s, facenum, turns):
    news = s.__copy__()
    
    news[facenum] = rotate_face(s, facenum, direction)
    updated_faces = rotate_edge(s, facenum, direction)
    for newf in updated_faces:
        news[newf] = updated_faces[newf]
    return news

#Rotates the values on a single face (not including the edges)
#0 -> clockwise
#1 -> counter
def rotate_face(s, facenum, direction):
    newf = copy_face(s[facenum])
    # if turns == 2:
    #     newf[0] = reversed(face[2])
    #     newf[2] = reversed(face[0])
    #     newf[1] = reversed(face[1])
    
    #Rotate clockwise
    if direction == 0:
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
        previous_tuple = edge_set[i-direction]
        #grab current face we are looking at
        curr_face = s[edge_tuple[0]]
        #grab previous face
        prev_face = s[previous_tuple[0]]
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
    if edge == 0:
        return face[edge]
    #Bottom edge is reversed because we want the values in clockwise order.
    #on the bottom this means they should be in order from right to left
    elif edge == 2:
        return reversed(face[edge])
    else:
        edge_list = []
        #j is the index within the row. (edge + 1) % 3 means edge 1 -> index 2
        #edge 3 -> index 0
        j = (edge + 1) % 4
        l = range(3)
        if edge == 3:
            l = reversed(l)
        for i in l:
            edge_list.append(face[i][j])
        return edge_list
        
def set_edge(face, edge, new_edge):
    newf = copy_face(face)
    if edge == 0: 
        newf[edge] = new_edge
    elif edge == 2:
        newf[edge] = reversed(new_edge)
    else:
        edge_list = []
        #j is the index within the row. (edge + 1) % 3 means edge 1 -> index 2
        #edge 3 -> index 0
        j = (edge + 1) % 4
        l = range(3)
        n = 0
        #Reverse row index if edge = 3
        if edge == 3:
            l = reversed(l)
        for i in l:
            newf[i][j] = new_edge[n]
            n += 1
    
    return newf
    

def copy_face(face):
    newf = []
    for row in face:
        newf.append(row)

    return newf

def goal_test(s):
    return s.d == complete

def goal_message(s):
    return "Rubik's cube is solved!"

class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)

def h_hamming(state):
    # "Counts the number of disks NOT at the destination peg."
    # n = 0
    # for i in range(0,9):
    #     if not state.d[i] == complete[i]:
    #         n += 1

    # return n

def h_euclidean(s):
    # total = 0.0
    # for i in range(0,9):
    #     horizontal = 0.0
    #     vertical = 0.0
    #     n = s.d[i]
    #     if not i%3==n%3:
    #         if i%3==1 or n%3==1:
    #             horizontal += 1
    #         else:
    #             horizontal += 2
    #     if not i//3==n//3:
    #         if i//3==1 or n//3==1:
    #             vertical += 1
    #         else:
    #             vertical += 2

    #     #print("tile: " + str(i))
    #     #print(horizontal)
    #     #print(vertical)
    #     hypotenuse = (horizontal**2+vertical**2)**(0.5)
    #     total += hypotenuse
    #     #print(hypotenuse)
    # return total

def h_manhattan(s):
    # total = 0
    # for i in range(0,9):
    #     horizontal = 0
    #     vertical = 0
    #     n = s.d[i]
    #     if not i%3==n%3:
    #         if i%3==1 or n%3==1:
    #             horizontal = 1
    #         else:
    #             horizontal = 2
    #     if not i//3==n//3:
    #         if i//3==1 or n//3==1:
    #             vertical = 1
    #         else:
    #             vertical = 2
    #     #print("tile: " + str(i))
    #     #print(horizontal)
    #     #print(vertical)

    #     total = total + horizontal + vertical
    # return total

def h_custom(s):
    # 'My custom heuristic takes the average of hamming, euclidean, and manhattan heuristics.'
    # total = h_hamming(s) + h_euclidean(s) + h_manhattan(s)
    # return total/3


#[0]Top, [1]left, [2]front, [3]bottom, [4]right, [5]back
complete3 = [[\
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

complete2 = [[\
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

class State():
    def __init__(self, d):
        self.d = d

    def __str__(self):
        # Produces a brief textual description of a state.
        d = self.d
        txt = ""
        for i in range(0, 9):
            txt = txt+"["+str(d[i])+"]"
            if i%3==2:
                txt+="\n"

        return txt

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
            newface = []
            for row in face:
                newface.append(row)
            news.d.append(newface)
        
        return news

    def __lt__(self, s2):
        return True



a = [1, 0, 2, 3, 4, 5, 6, 7, 8]
b = [3, 1, 2, 4, 0, 5, 6, 7, 8]
c = [1, 4, 2, 3, 7, 0, 6, 8, 5]
a10 = [4, 5, 0, 1, 2, 3, 6, 7, 8]
a12 = [3, 1, 2, 6, 8, 7, 5, 4, 0]
a14 = [4, 5, 0, 1, 2, 8, 3, 7, 6]
a16 = [0, 8, 2, 1, 7, 4, 3, 6, 5]
INITIAL_STATE = State(a10)
CREATE_INITIAL_STATE = lambda: INITIAL_STATE


# Calculate all possible legal movement combinations
# Operations (0-5), turns (0-2 single direction clockwise)
# top, left, front, right, bottom, back
combinations = []
combinations = list(itertools.product(range(6),[-1,1]))


#peg_combinations = [('tile '+str(a),'tile '+str(b)) for (a,b) in combinations]
OPERATORS = [Operator("Rotate face "+str(p),
                      #lambda s,p1=p: can_move(s,p1),
                      # The default value construct is needed
                      # here to capture the values of p&q separately
                      # in each iteration of the list comp. iteration.
                      lambda s,p1=p, q1=q: move(s,p1, q1) )
             for (p, q) in combinations]

GOAL_TEST = lambda s: goal_test(s)

GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)

HEURISTICS = {'h_hamming': h_hamming, 'h_euclidean':h_euclidean, 'h_manhattan': h_manhattan, 'h_custom': h_custom}

