from collections import defaultdict


class Board:

    def __init__(self, size):
        self.__size = size
        self.__free_steps = set((i, j) for i in range(self.__size) for j in range(self.__size))
        self._done_steps = defaultdict(set)
        self.board = [[0 for _ in range(self.__size)] for _ in range(self.__size)]

    def add_step(self, step: tuple[int, int], symbol: str):
        if step in self.__free_steps:
            self._done_steps[symbol].add(step)
            self.__free_steps.remove(step)
            self.board[step[0]][step[1]] = symbol
        else:
            raise ValueError("Ячейка не существует или занята")

    def board_match(self) -> bool:
        def chek_line(line):
            line_set = set(line)
            if 0 not in line_set and len(line_set) == 1:
                raise ValueError("CHECK_LINE")
            return False

        board_len = len(self.board)
        diagonal = map(lambda idx: self.board[idx][idx], range(0, board_len))
        diagonal_invert = map(lambda idx: self.board[idx][board_len - idx - 1], range(board_len - 1, -1, -1))
        try:
            _ = any(map(chek_line, (diagonal, diagonal_invert)))
            for row, column in zip(self.board, zip(*self.board)):
                _ = any(map(chek_line, (row, column)))
        except ValueError as exc:
            if 'CHECK_LINE' in exc.args:
                return True
            else:
                raise exc
        return False

    def get_free_cells(self) -> set:
        return self.__free_steps

    def get_done_steps(self) -> dict:
        return dict(self._done_steps)

    def __str__(self):
        separator = '#' * self.__size * 2 + '##'
        title_row = f'  {" ".join(map(str, list(range(self.__size))))}'
        rows = ""
        for idx, row in enumerate(self.board):
            rows += f'{idx} {"|".join(f"{i}" for i in row)}\n'

        return f"{separator}\n{title_row}\n{rows}{separator}"
