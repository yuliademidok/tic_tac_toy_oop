from src.board import Board
from src.constants import SYMBOLS
from src.game import Game
from src.templates import user_interface
from src.user import HumanPlayer, CompPlayer


class Lobby:
    user_interface("welcome")

    def __init__(self, board_size=3):
        self.board = Board(board_size)
        self.mode = self.__ask_mode()
        self.users = tuple(i() for i in self.__modes[self.mode])
        self.game = Game(self.users, self.board)

    __modes = {
        "USER": (lambda: HumanPlayer(SYMBOLS[0]), lambda: HumanPlayer(SYMBOLS[1])),
        "COMP": (lambda: HumanPlayer(SYMBOLS[0]), lambda: CompPlayer(SYMBOLS[1])),
    }

    def __ask_mode(self) -> str:
        user_modes = {idx: itm for idx, itm in enumerate(self.__modes, 1)}

        modes_str = "\n".join(f"{key}: {value}" for key, value in user_modes.items())
        modes_string = f"Выберите номер режима игры\n{modes_str}"

        while True:
            try:
                mode_input = int(input(modes_string))
                return user_modes[mode_input]
            except ValueError:
                print(user_interface("invalid_mode_value"))
            except KeyError:
                print(user_interface("invalid_mode_key"))
            continue

    # @staticmethod
    # def ask_new_game() -> bool:
    #     variants = ('Y', 'N')
    #
    #     while True:
    #         user_answer = input(f"Желаете начать новую игру? {'/'.join(variants)}").upper()
    #         if user_answer in variants:
    #             return user_answer == variants[0]
    #         print("Ошибка ввода, введите верное значение")

    def main(self):
        self.game.start()
