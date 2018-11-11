# Derek Wang

# Rubiks Cube Representation

# In order to do this project, we need to define a Rubiks Cube and all provide state management
# An agent should be able to perform any of the different rotations which will allow the agent to solve the cube.

# We will construct this with a 3x3x3 traditional Rubik's Cube in mind but account for variable size

import random

class Cube:
    # Init the cube using a give size
    def __init__(self,size=3):
        self.__size__ = size
        self.__front__ = [[0 for x in range(self.__size__)] for x in range(self.__size__)]
        self.__left__ = [[1 for x in range(self.__size__)] for x in range(self.__size__)]
        self.__back__ = [[2 for x in range(self.__size__)] for x in range(self.__size__)]
        self.__top__ = [[3 for x in range(self.__size__)] for x in range(self.__size__)]
        self.__right__ = [[4 for x in range(self.__size__)] for x in range(self.__size__)]
        self.__bottom__ = [[5 for x in range(self.__size__)] for x in range(self.__size__)]
        
    def set_front(self, l):
        if len(l) == self.__size__ & len(l[0]) == self.__size__ & len(l[1]) == self.__size__ & len(l[2]) == self.__size__:
            self.__front__ = l
        else:
            raise Exception("Input lists incorrect length")

    def set_left(self, l):
        if len(l) == self.__size__ & len(l[0]) == self.__size__ & len(l[1]) == self.__size__ & len(l[2]) == self.__size__:
            self.__left__ = l
        else:
            raise Exception("Input lists incorrect length")

    def set_back(self, l):
        if len(l) == self.__size__ & len(l[0]) == self.__size__ & len(l[1]) == self.__size__ & len(l[2]) == self.__size__:
            self.__back__ = l
        else:
            raise Exception("Input lists incorrect length")

    def set_top(self, l):
        if len(l) == self.__size__ & len(l[0]) == self.__size__ & len(l[1]) == self.__size__ & len(l[2]) == self.__size__:
            self.__top__ = l
        else:
            raise Exception("Input lists incorrect length")

    def set_right(self, l):
        if len(l) == self.__size__ & len(l[0]) == self.__size__ & len(l[1]) == self.__size__ & len(l[2]) == self.__size__:
            self.__right__ = l
        else:
            raise Exception("Input lists incorrect length")

    def set_bottom(self, l):
        if len(l) == self.__size__ & len(l[0]) == self.__size__ & len(l[1]) == self.__size__ & len(l[2]) == self.__size__:
            self.__bottom__ = l
        else:
            raise Exception("Input lists incorrect length")

    def get_front(self):
        """
        Get the front face of the cube
        """
        return self.__front__
    
    def get_back(self):
        """
        Get the back face of the cube
        """
        return self.__back__
    
    def get_left(self):
        """
        Get the back face of the cube
        """
        return self.__left__

    def get_right(self):
        """
        Get the back face of the cube
        """
        return self.__right__

    def get_top(self):
        """
        Get the back face of the cube
        """
        return self.__top__

    def get_bottom(self):
        """
        Get the back face of the cube
        """
        return self.__bottom__


    def rotate_face(self, matrix):
        """
        Takes in the 2 dimentional face representation and performs the matrix operation of clockwise rotation
        The new matrix is returned
        """
        temp = [[],[],[]] # Generate the new matrix
        for x in reversed(range(self.__size__)):
            for y in range(self.__size__):
                temp[y].append(matrix[x][y])
        return temp

    def rotate_front(self):
        """
        Rotate front face of the cube
        """
        # Rotate the face itself clockwise
        self.__front__ = self.rotate_face(self.__front__)
        # Perform the rotations on the edges
        # The top and bottom edges can save values before transfer
        new_top = [self.__left__[row][-1] for row in reversed(range(self.__size__))]
        new_bottom = [self.__right__[row][0] for row in reversed(range(self.__size__))]
        # Transfer top and bottom to the sides
        # Top to right
        for idx in range(self.__size__):
            self.__right__[idx][0] = self.__top__[-1][idx]

        # Bottom to left
        for idx in range(self.__size__):
            self.__left__[idx][-1] = self.__bottom__[0][idx]
        
        # Replace the top and bottom
        self.__top__[-1] = new_top
        self.__bottom__[0] = new_bottom
      
    def rotate_back(self):
        """
        Rotate back face of the cube
        """
        # Rotate the face itself clockwise
        self.__back__ = self.rotate_face(self.__back__)

        new_top = [self.__right__[row][-1] for row in range(self.__size__)]
        new_bottom = [self.__left__[row][0] for row in range(self.__size__)]
        # Transfer top and bottom to the sides
        # Top to right face in this orientation
        for idx in range(self.__size__):
            self.__left__[idx][0] = self.__top__[0][-1 - idx]

        # Bottom to left
        for idx in range(self.__size__):
            self.__right__[idx][-1] = self.__bottom__[-1][-1 - idx]
    
        # Replace the top and bottom
        self.__top__[0] = new_top
        self.__bottom__[-1] = new_bottom

    def rotate_left(self):
        """
        Rotate left face of the cube
        """
        # Rotate the face itself clockwise
        self.__left__ = self.rotate_face(self.__left__)

        # Grab the actual data being moved
        new_top = [self.__back__[row][-1] for row in reversed(range(self.__size__))]
        new_bottom = [self.__front__[row][0] for row in reversed(range(self.__size__))]

        new_right = [self.__top__[idx][0] for idx in range(self.__size__)]
        new_left = [self.__bottom__[idx][0] for idx in reversed(range(self.__size__))]

        # Transfer top and bottom to the sides
        # Top to right face in this orientation
        for idx in range(self.__size__):
            # Back to top
            self.__top__[idx][0] = new_top[idx]
            # Front to bottom
            self.__bottom__[idx][0] = new_bottom[::-1][idx]
            # top to front
            self.__front__[idx][0] = new_right[idx]
            # bottom to back
            self.__back__[idx][-1] = new_left[idx]

    def rotate_right(self):
        """
        Rotate right side clockwise
        """
        # Rotate the face itself clockwise  
        self.__right__ = self.rotate_face(self.__right__)

        # Grab the actual data being moved
        new_top = [self.__front__[row][-1] for row in range(self.__size__)]
        new_bottom = [self.__back__[row][0] for row in reversed(range(self.__size__))]

        new_right = [self.__top__[idx][-1] for idx in reversed(range(self.__size__))]
        new_left = [self.__bottom__[idx][-1] for idx in range(self.__size__)]

        # Transfer top and bottom to the sides
        # Top to right face in this orientation
        for idx in range(self.__size__):
            # Back to top
            self.__top__[idx][-1] = new_top[idx]
            # Front to bottom
            self.__bottom__[idx][-1] = new_bottom[idx]
            # top to front
            self.__front__[idx][-1] = new_left[idx]
            # bottom to back
            self.__back__[idx][0] = new_right[idx]

    def rotate_top(self):
        """
        Rotate top clockwise
        """
        #grab bottom row of front, left, right, back
        temp = []
        temp = self.__front__[0]
        self.__front__[0] = self.__right__[0]
        self.__right__[0] = self.__back__[0]
        self.__back__[0] = self.__left__[0]
        self.__left__[0] = temp

        # Rotate the face itself clockwisez 
        self.__top__ = self.rotate_face(self.__top__)

    def rotate_bottom(self):
        """
        Rotate bottom face clockwise
        """
        #grab bottom row of front, left, right, back
        temp = []
        temp = self.__front__[2]
        self.__front__[2] = self.__left__[2]
        self.__left__[2] = self.__back__[2]
        self.__back__[2] = self.__right__[2]
        self.__right__[2] = temp
        # Rotate the face itself clockwise
        self.__bottom__ = self.rotate_face(self.__bottom__)

    def get_size(self):
        """
            Returns the n dimension of the cube
            """
        return self.__size__

    def __printer__(self, top, left, front, right, back, bottom):
        """
        Print the faces with the orientation of 

            T
        L  F  R  Ba
            Bo   
        """
        for row in top:
            print("          " + str(row))
        for idx in range(self.__size__):
            print(str(left[idx]) + " " + str(front[idx]) + " " + str(right[idx]) + " " + str(back[idx]))
        for row in bottom:
            print("          " + str(row)) 

    def print_cube(self, orientation="front"):
        """
        Switch the print case depending on the given orientation
        """
        if orientation == "front":
            self.__printer__(self.__top__, self.__left__, self.__front__, self.__right__, self.__back__, self.__bottom__)
        # TODO: Put in the methods for orientation of different faces being the front
        # This probably requires the use of matrix rotations for the top and bottom faces

    def is_solved(self):
        """
        Checks that the rubik's cube is solved. This can mean that each face has the same numeral in the 3x3 matrix
        Uses the center pieces which shouldn't move to determine what goes where
        """
        solved = True
        if self.__front__ != [[self.__front__[1][1] for x in range(self.__size__)] for x in range(self.__size__)]:
            solved = False
        if self.__back__ != [[self.__back__[1][1] for x in range(self.__size__)] for x in range(self.__size__)]:
            solved = False
        if self.__left__ != [[self.__left__[1][1] for x in range(self.__size__)] for x in range(self.__size__)]:
            solved = False
        if self.__right__ != [[self.__right__[1][1] for x in range(self.__size__)] for x in range(self.__size__)]:
            solved = False
        if self.__top__ != [[self.__top__[1][1] for x in range(self.__size__)] for x in range(self.__size__)]:
            solved = False
        if self.__bottom__ != [[self.__bottom__[1][1] for x in range(self.__size__)] for x in range(self.__size__)]:
            solved = False
        # If we had no issues then the cube should be solved
        return solved

    def scramble(self, moves=20):
        """
        For the given number of moves, randomly turn the cube to scramble it.
        """
        for x in range(moves):
            r = random.randint(0, 5)
            if r == 0:
                self.rotate_front()
            elif r == 1:
                self.rotate_back()
            elif r == 2:
                self.rotate_left()
            elif r == 3:
                self.rotate_right()
            elif r == 4:
                self.rotate_top()
            elif r == 5:
                self.rotate_bottom()
        