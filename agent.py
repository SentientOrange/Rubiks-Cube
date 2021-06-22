"""
Define the Q learning algorithm via the agent class
"""
from typing import List

from cube import Cube, Move


class Agent:
    def __init__(self) -> None:
        self.moves_list = []

    def solve(self, cube: Cube) -> None:
        raise NotImplementedError

    def get_moves(self) -> List[Move]:
        return self.moves_list


class QAgent(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.mem = {}

    def get_state(self, cube: Cube) -> None:
        """
        Condense a cube's state into something that takes up less memory
        """
        pass

    def get_next_move(self, cube: Cube) -> Move:
        return Move.random_move(cube.size)

    def solve(self, cube: Cube) -> None:
        while not cube.solved():
            move = self.get_next_move(cube)
            self.moves_list.append(move)
            cube.rotate(move)
