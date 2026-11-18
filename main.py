from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

from chess_game import ChessGame


if __name__ == "__main__":
    ChessGame().run()