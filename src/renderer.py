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
        """
        :param board:
        board takes in type of Board().
        :param selected_piece:
         selected_piece is used to highlight the (row,col) of the selected_piece.

        :param valid_moves:
        valid_moves is used to highlight with dots the valid moves the selected_piece can do.
        """
        checked_kings = {
            board.find_king(color)
            for color in ("w", "b")
            if board.is_in_check(color)
        }

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

                if (row, col) == selected_piece:
                    highlight_surface = pygame.Surface((SQ_SIZE, SQ_SIZE), pygame.SRCALPHA)
                    highlight_surface.fill((255, 255, 0, 120))  # Translucent yellow
                    self.screen.blit(highlight_surface, square.topleft)
                    pygame.draw.rect(self.screen, (255, 215, 0), square, 4)

                if (row, col) in checked_kings:
                    pygame.draw.rect(self.screen, (180, 0, 0), square, 4)
