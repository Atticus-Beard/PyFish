class Board:
    def __init__(self):
        self.grid = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]

    def get_piece(self, position):
        row, col = position
        return self.grid[row][col]

    def is_empty(self, position):
        return self.get_piece(position) == "--"

    def move(self, start, end):
        piece = self.get_piece(start)
        row, col = end
        start_row, start_col = start

        self.grid[row][col] = piece
        self.grid[start_row][start_col] = "--"

    def is_valid_move(self, start, end) -> bool:
        start_row, start_col = start
        end_row, end_col = end

        piece = self.grid[start_row][start_col]
        target = self.grid[end_row][end_col]

        if start == end:
            return False

        # Makes sure the piece is not capturing its own color.
        if target != "--" and piece[0] == target[0]:
            return False

        piece_color = piece[0]
        piece_type = piece[1]

        row_diff = end_row - start_row
        col_diff = end_col - start_col

        # --- ROOK RULES ---
        if piece_type == 'R':
            if row_diff != 0 and col_diff != 0:
                return False

            # Check for path blocking.
            if piece_type == 'R':
                if row_diff != 0 and col_diff != 0:
                    return False

                # Check for path blocking.
                if row_diff == 0:
                    # Horizontal movement
                    step = 1 if col_diff > 0 else -1

                    for c in range(start_col + step, end_col, step):
                        if self.grid[start_row][c] != "--":
                            return False

                elif col_diff == 0:
                    # Vertical movement
                    step = 1 if row_diff > 0 else -1

                    for r in range(start_row + step, end_row, step):
                        if self.grid[r][start_col] != "--":
                            return False


        # --- BISHOP RULES ---
        elif piece_type == "B":
            # Checks that the bishop is moving only diagonally
            if abs(col_diff) != abs(row_diff):
                return False

            # Check for path blocking (step diagonally in both row and col directions)
            row_step = 1 if row_diff > 0 else -1
            col_step = 1 if col_diff > 0 else -1

            curr_row, curr_col = start_row + row_step, start_col + col_step

            # Goes through all the steps of the bishop rules and validates that the piece did not hop over any pieces.
            while (curr_row, curr_col) != (end_row, end_col):
                if self.grid[curr_row][curr_col] != "--":
                    return False

                curr_row += row_step
                curr_col += col_step

            return True

        # --- PAWN RULES ---
        elif piece_type == "P":
            direction = -1 if piece_color == "w" else 1
            start_row_base = 6 if piece_color == "w" else 1

            # Move forward one square
            if col_diff == 0 and row_diff == direction and target == "--":
                return True

            # Move forward two squares (initial move)
            if col_diff == 0 and row_diff == 2 * direction and start_row == start_row_base and target == "--":
                intermediate_row = start_row + direction
                if self.grid[intermediate_row][start_col] != "--":
                    return False

                return True

            # Pawn captures diagonally
            if abs(col_diff) == 1 and row_diff == direction and target != "--":
                return True

            return False

        # --- QUEEN RULES ---
        elif piece_type == "Q":
            # Must move either straight (rook-like) or diagonally (bishop-like)
            is_straight = (row_diff == 0 or col_diff == 0)
            is_diagonal = (abs(row_diff) == abs(col_diff))

            if not is_straight and not is_diagonal:
                return False

            row_step = 1 if row_diff > 0 else (-1 if row_diff < 0 else 0)
            col_step = 1 if col_diff > 0 else (-1 if col_diff < 0 else 0)

            curr_row, curr_col = start_row + row_step, start_col + col_step
            while (curr_row, curr_col) != (end_row, end_col):
                if self.grid[curr_row][curr_col] != "--":
                    return False

                curr_row += row_step
                curr_col += col_step

            return True

        # --- KNIGHT RULES ---
        elif piece_type == "N":
            is_l_shape = (abs(row_diff) == 2 and abs(col_diff) == 1) or (abs(row_diff) == 1 and abs(col_diff) == 2)

            if not is_l_shape:
                return False

            return True

        # Added king rules.

        elif piece_type == "K":
            if max(abs(row_diff), abs(col_diff)) != 1:
                return False
            return True

        return True