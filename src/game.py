from itertools import cycle

from src.game_result import GameResult
from src.logger import Logger
from src.templates import user_interface


class Game:
    def __init__(self, users, board):
        self.users = users
        self.board = board

    @Logger.log_game
    def start(self):
        winner = None
        step_num = None

        for step_num, user in enumerate(cycle(self.users), 1):
            print(f"Ход {step_num} игрока: {user}")
            print(self.board)
            self.__make_step(user, self.board)

            if self.board.board_match():
                winner = user
                print(GameResult(step_num, winner))
                break
            if step_num > 8:
                print(GameResult(step_num, winner))
                break

        return winner.name, step_num, self.board.get_done_steps()

    @staticmethod
    def __make_step(user, board):
        while True:
            step = user.get_step(board)
            try:
                board.add_step(step, user.symbol)
            except ValueError:
                user_interface("invalid_step")
                continue
            break
