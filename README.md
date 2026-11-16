# PyFish

PyFish is a lightweight chess game built with [Python](https://python.org) and [Pygame](https://www.pygame.org/). It provides a graphical 8×8 chessboard, chess piece artwork, turn tracking, move highlighting, and basic piece movement. PyFish is later going to have an autonomous second player.  

<img width="640" height="672" alt="Screenshot 2026-11-16 at 13 12 35" src="https://github.com/user-attachments/assets/e4040956-6722-4aad-a93c-0f5cdc2eafc0" />


## Features

- Graphical chessboard using Pygame
- White and black piece textures included in `images/`
- Alternating turns, with White moving first
- Highlighted selectable pieces and valid destinations
- Basic movement rules for pawns, rooks, bishops, knights, and queens
- Capturing of opposing pieces

## Requirements

- Python 3.8+
- Pygame

```bash
pip install pygame
```
  
## Installation

 1. Clone the repository to install PyFish.
```bash
git clone https://github.com/Atticus-Beard/PyFish.git
```

2. Install the dependency:
```bash 
python -m pip install -r requirements.txt
```

## Running the Game

From the project root (so the `images/` folder can be found):

```bash
python main.py
```

## How to play

1. White plays first.
2. Click one of your pieces to select it. The square is highlighted and valid moves appear as dots.
3. Click a destination square to move the piece. If the move is invalid, the selection is cleared.
4. Click on the same piece again to deselect it.
5. Turns alternate automatically after every valid move.

Close the window to quit the program.

## Project structure
```
.
├── main.py          # The game
├── images/          # Piece textures
│   ├── wR.png  wN.png  wB.png  wQ.png  wK.png  wP.png
│   └── bR.png  bN.png  bB.png  bQ.png  bK.png  bP.png
└── README.md
```

The `images/` folder must contain 12 PNG files, one per piece. Filenames are `<color><piece>.png`, where color is `w` (white) or `b` (black), and piece is one of:


| Code | Piece  |
|------|--------|
| `R`  | Rook   |
| `N`  | Knight |
| `B`  | Bishop |
| `Q`  | Queen  |
| `K`  | King   |
| `P`  | Pawn   |

Images are scaled automatically to fit each square (80x80 px)


## How it works

- **Board State** is a 2d list of two-character strings, such as ```"wP"``` for a white pawn or ```"--"``` for an empty square.
- **```is_valid_move(board, start, end)```** checks a move to see if it is valid against the rules for that piece.
- **```draw_board```** and **```draw_pieces```** render the squares, highlights, move indicators, and piece sprites each frame.
- **`main`** runs the event loop, handles mouse clicks, and tracks the selected piece and whose turn it is.


## Roadmap / Known limitations

This is a work in progress. The following are not implemented.

- [ ] **Check, checkmate, and stalemate** detection
- [ ] **Castling**
- [ ] **En passant**
- [ ] **Pawn Promotion**
- [ ] Game-over / win screen and reset
- [ ] Bot player

## Credits

The board colors come from [chess.com](https://chess.com).

The piece images are from [Wikimedia Commons](https://commons.wikimedia.org/) and are included in the ```/images``` folder. See Wikimedia Commons for each image's license and attribution requirements. 

PyFish is named after [Stock Fish](https://stockfishchess.org/).
