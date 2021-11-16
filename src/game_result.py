
class GameResult:
    def __init__(self, step_num, name):
        self.step_num = step_num
        self.name = name

    def win(self):
        return f"Победил игрок {self.name} на ходу {self.step_num}"

    def draw(self):
        return f"На ходу {self.step_num} произошла ничья"

    def __str__(self):
        if self.name:
            return self.win()
        return self.draw()
