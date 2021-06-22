"""
Define a Rubiks cube that is fast to manipulate and extendable to various sizes

The important part here is that a "move" is fast and determination of
correctness is fast so that the agent can evaluate states quickly and
converge on an acceptable strategy.

Rotation Strategy

It may simplify things if the cube representation assumes a fixed orientation.
The "rotations" can be one way operations that are mutative but algorithmically consistent

       1  2  3
    a [a][a][a]
    b [a][a][a]
    c [a][a][a]
"""
from enum import Enum
from random import choice, randint
from typing import List


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    WHITE = 4
    YELLOW = 5
    ORANGE = 6


class Plane(Enum):
    X = 1
    Y = 2
    Z = 3


class Move:
    def __init__(self, idx: int, plane: Plane, clockwise: bool) -> None:
        self.idx = idx
        self.plane = plane
        self.clockwise = clockwise

    def __str__(self):
        c = "clockwise" if self.clockwise else "counter-clockwise"
        return f"Move rotated {self.plane} {self.idx} index {c}"

    def __repr__(self):
        return f"Move({self.idx}, {self.plane}, {self.clockwise})"

    @classmethod
    def random_move(cls, size: int):
        p = choice(list(Plane))
        c = randint(0, 1) == 1
        idx = randint(0, size - 1)
        return Move(idx, p, c)

    def reverse(self):
        return Move(self.idx, self.plane, not self.clockwise)


class CubeSide:
    def __init__(self, name: str, size: int, init_color: Color):
        self.name = name
        self.size = size
        self.state = [[init_color for _ in range(size)] for _ in range(size)]

    def get_col(self, idx: int, rev: bool = False) -> List[Color]:
        ret = [row[idx] for row in self.state]
        if rev:
            ret.reverse()
        return ret

    def get_row(self, idx: int, rev: bool = False) -> List[Color]:
        ret = [x for x in self.state[idx]]
        if rev:
            ret.reverse()
        return ret

    def check(self) -> bool:
        target: Color = self.state[0][0]
        for row in self.state:
            if not all(cell == target for cell in row):
                return False
        return True

    def apply_change(self, change: List[Color], idx: int, col: bool = False):
        if col:
            for i in range(self.size):
                self.state[i][idx] = change[i]
        else:
            for i in range(self.size):
                self.state[idx] = change

    def rotate(self, clockwise: bool = True):
        new_state = [[] for _ in range(self.size)]
        for row in self.state:
            for idx, val in enumerate(row):
                if clockwise:
                    new_state[idx].insert(0, val)
                else:
                    new_state[self.size - 1 - idx].append(val)
        self.state = new_state

    def print(self):
        print(self.name)
        print("\n======\n")
        for row in self.state:
            print(row)
        print()


class Cube:
    def __init__(self, size: int = 3) -> None:
        self.size = size
        # Initialize the cube state
        self.front = CubeSide("front", self.size, Color.BLUE)
        self.back = CubeSide("back", self.size, Color.GREEN)
        self.left = CubeSide("left", self.size, Color.WHITE)
        self.right = CubeSide("right", self.size, Color.YELLOW)
        self.top = CubeSide("top", self.size, Color.ORANGE)
        self.bottom = CubeSide("bottom", self.size, Color.RED)

        self.sides = (
            self.front,
            self.back,
            self.left,
            self.right,
            self.top,
            self.bottom,
        )

        # Preload choices so we don't have to recreate a list every time
        self.plane_choices = list(Plane)

    def rotate(self, m: Move):
        """
        Perform a rotation
        """
        # Realign rotation. This is pretty much hard coded stuff since it's a cube
        # and should be a little faster than having to figure it out

        index = m.idx
        plane = m.plane
        clockwise = m.clockwise

        if plane == Plane.X:
            # Horizontal
            if index == 0:
                self.top.rotate(clockwise)
            elif index == self.size - 1:
                self.bottom.rotate(not clockwise)
            front_save = self.front.get_row(index)
            if clockwise:
                self.front.apply_change(self.right.get_row(index), index)
                self.right.apply_change(self.back.get_row(index), index)
                self.back.apply_change(self.left.get_row(index), index)
                self.left.apply_change(front_save, index)
            else:
                self.front.apply_change(self.left.get_row(index), index)
                self.left.apply_change(self.back.get_row(index), index)
                self.back.apply_change(self.right.get_row(index), index)
                self.right.apply_change(front_save, index)
        elif plane == Plane.Y:
            # Horizontal
            if index == 0:
                self.left.rotate(clockwise)
            elif index == self.size - 1:
                self.right.rotate(not clockwise)
            front_save = self.front.get_col(index)
            if clockwise:
                self.front.apply_change(self.top.get_col(index), index, True)
                self.top.apply_change(
                    self.back.get_col(self.size - 1 - index, True), index, True
                )
                self.back.apply_change(
                    self.bottom.get_col(index, True),
                    self.size - 1 - index,
                    True,
                )
                self.bottom.apply_change(front_save, index, True)
            else:
                self.front.apply_change(self.bottom.get_col(index), index, True)
                self.bottom.apply_change(
                    self.back.get_col(self.size - 1 - index, True), index, True
                )
                self.back.apply_change(
                    self.top.get_col(index, True), self.size - 1 - index, True
                )
                self.top.apply_change(front_save, index, True)
        elif plane == Plane.Z:
            if index == 0:
                self.front.rotate(clockwise)
            elif index == self.size - 1:
                self.back.rotate(not clockwise)
            right_save = self.right.get_col(index)
            if clockwise:
                self.right.apply_change(
                    self.top.get_row(self.size - 1 - index), index, True
                )
                self.top.apply_change(
                    self.left.get_col(self.size - 1 - index, True),
                    self.size - 1 - index,
                )
                self.left.apply_change(
                    self.bottom.get_row(index),
                    self.size - 1 - index,
                    True,
                )
                right_save.reverse()
                self.bottom.apply_change(right_save, index)
            else:
                self.right.apply_change(self.bottom.get_row(index, True), index, True)
                self.bottom.apply_change(
                    self.left.get_col(self.size - 1 - index), index
                )
                self.left.apply_change(
                    self.top.get_row(self.size - 1 - index, True),
                    self.size - 1 - index,
                    True,
                )
                self.top.apply_change(right_save, self.size - 1 - index)

    def scramble(self, turns: int = 15):
        """
        Randomly mutate the cube into a valid scrambled state

        Args:
            turns: Number of turns to randomly turn
        """
        for _ in range(turns):
            # randint is inclusive
            m = Move.random_move(self.size)
            self.rotate(m)

    def solved(self) -> bool:
        """
        Checks if the cube is solved yet
        """
        return all(side.check() for side in self.sides)

    def print(self) -> None:
        """
        Print out a representation of the cube to the command line
        """
        for side in self.sides:
            side.print()
