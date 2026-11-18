import pygame
from config import DIMENSION, SQ_SIZE, DARK_RGB, LIGHT_RGB

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.images = {}
        self.load_pieces()

    def load_pieces(self):
        """ Loads the piece textures from the 'images' directory. '"""
        pieces = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wP', 'bR', 'bN', 'bB', 'bQ', 'bK', 'bP']
        for piece in pieces:
            self.images[piece] = pygame.transform.smoothscale(
                pygame.image.load(f"images/{piece}.png"), (SQ_SIZE, SQ_SIZE),
            )

    def draw_board(self, board, selected_piece, valid_moves):
        for row in range(DIMENSION):
            for col in range(DIMENSION):
                color = (
                    LIGHT_RGB
                    if (row + col) % 2 == 0
                    else DARK_RGB
                )
                square = pygame.Rect(
                    col * SQ_SIZE,
                    row * SQ_SIZE,
                    SQ_SIZE,
                    SQ_SIZE,
                )
                pygame.draw.rect(self.screen, color, square)

                if (row, col) in valid_moves:
                    center = square.center
                    pygame.draw.circle(
                        self.screen,
                        (202, 203, 179),
                        center,
                        SQ_SIZE // 6,
                    )

                piece = board.get_piece((row, col))
                if piece != "--":
                    self.screen.blit(
                        self.images[piece],
                        square,
                    )

