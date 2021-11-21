from pathlib import Path

COMP_NAMES = [
    "R2D2",
    "C3PO",
    "WALLE",
    "DALEK",
]

SYMBOLS = ("X", "Y")

FILES = {
    "GAME_INIT": "game_init",
    "GAME_LOG": "game_log",
}

ROOT_DIR = Path(__file__).parent.parent

log_columns = {
    "init_game": ("game_number",
                  'start_time',
                  "user1",
                  "user2"),
    "game_log": ('game_number',
                 'winner_name',
                 'game_steps',)
}
