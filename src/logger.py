import os
import functools

from src.constants import FILES, ROOT_DIR, log_columns


class Logger:
    delim = ';'

    # def write(self, data: str, handler: str, mode="a"):
    #     file = os.path.join(ROOT_DIR, "logs", FILES[handler])
    #     with open(file, mode, encoding="UTF-8") as f:
    #         f.writelines(str(data) + self.delim)

    @staticmethod
    def log_game(func):
        @functools.wraps(func)
        def wrap(cls, *args, **kwargs):
            data = func(cls, *args, **kwargs)
            file = os.path.join(ROOT_DIR, "logs", FILES["GAME_LOG"])

            with open(file, "a", encoding="UTF-8") as file:
                file.writelines(";".join(map(str, data)) + '\n')

            return data
        return wrap
