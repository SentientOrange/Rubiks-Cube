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

    def solve(self, cube: Cube) -> None:
        pass
