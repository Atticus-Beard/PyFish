import pygame
from .board import Board
from .renderer import Renderer
from config import WIDTH, HEIGHT, SQ_SIZE, FPS, DIMENSION


class ChessGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("PyFish Game")

        self.clock = pygame.time.Clock()
        self.renderer = Renderer(screen=self.screen)
        self.board = Board()

        self.selected_piece = ()
        self.valid_moves = []
        self.turn = "w"
        self.running = True

    def handle_click(self):
        col = pygame.mouse.get_pos()[0] // SQ_SIZE
        row = pygame.mouse.get_pos()[1] // SQ_SIZE
        position = (row, col)

        # Deselect the selected piece.
        if position == self.selected_piece:
            self.valid_moves = []
            self.selected_piece = ()
            return

        # First click: select a piece.
        if not self.selected_piece:
            piece = self.board.get_piece(position)

            if piece == "--" or piece[0] != self.turn:
                return

            self.selected_piece = position
            self.valid_moves = []

            for r in range(DIMENSION):
                for c in range(DIMENSION):
                    if self.board.is_legal_move(position, (r, c)):
                        self.valid_moves.append((r, c))
            return

        # Second click: try to move the selected piece.
        if self.board.is_legal_move(self.selected_piece, position):
            self.board.move(self.selected_piece, position)
            self.turn = "b" if self.turn == "w" else "w"

            if self.board.is_checkmate(self.turn):
                winner = "b" if self.turn == "w" else "w"

                # Handle win screen here.
                print(
                    f"Checkmate - {'White' if winner == 'w' else 'Black'} wins!"
                )

            if self.board.is_stalemate(self.turn):
                print(
                    f"Stalemate. There was no legal moves for {'White' if self.turn == 'w' else 'Black'}."
                )


        self.selected_piece = ()
        self.valid_moves = []

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click()

            self.renderer.draw_board(
                self.board,
                self.selected_piece,
                self.valid_moves,
            )

            pygame.display.flip()
            self.clock.tick(FPS)