import random

from src.board import Board
from src.constants import COMP_NAMES
from src.templates import user_interface


class CompPlayer:

    def __init__(self, symbol, name=None):
        self.symbol = symbol
        self.name = self._get_name(name)

    def _get_name(self, name):
        if name:
            return name
        return random.choice(COMP_NAMES)

    def get_step(self, board: Board):
        return random.choice(tuple(board.get_free_cells()))

    def __str__(self):
        return self.name


class HumanPlayer(CompPlayer):

    def _get_name(self, name):
        if name:
            return name
        user_input = user_interface("enter_name")
        return user_input

    def get_step(self, board: Board):
        result = []
        input_step = user_interface("ask_step")
        steps = input_step.split(" ")
        try:
            if len(steps) != 2:
                raise ValueError
            for itm in steps:
                result.append(int(itm))
        except ValueError:
            pass
        return tuple(result)
