import pygame as p
import ChessEngine

# Initializing constants
WIDTH = HEIGHT = 512
DIMENSION = 8  # Chessboard is 8x8
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # For animations
IMAGES = {}

# Image loading function
def loadImages():
    pieces = ['bK', 'bN', 'bB', 'bR', 'bQ', 'bP', 'wK', 'wN', 'wB', 'wR', 'wQ', 'wP']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f'images/{piece}.png'), (SQUARE_SIZE, SQUARE_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()  # Get initial valid moves
    moveMade = False  # Flag to check if a move was made
    loadImages()
    running = True
    sqSelected = ()  # No square selected initially
    playerClicks = []  # Stores [(start_row, start_col), (end_row, end_col)]
    
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            # Mouse handling
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQUARE_SIZE
                row = location[1] // SQUARE_SIZE
                
                # If the same square is clicked twice, reset
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                
                # After 2 clicks, attempt to make a move
                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    
                    # Check if the first click is a valid piece (not empty)
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                        sqSelected = ()  # Reset selection
                        playerClicks = []  # Reset clicks
                    #Player clicked on second piece without a valid move
                    else:
                        playerClicks = [sqSelected]
            # Key handling
            elif e.type == p.KEYDOWN:
                # Undo key (z key)
                if e.key == p.K_z:
                    gs.undoMove()
                    moveMade = True
        if moveMade:
            validMoves = gs.getValidMoves()  # Update valid moves after a move is made
            moveMade = False  # Reset move made flag
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

# Game state drawing function
def drawGameState(screen, gs):
    drawBoard(screen)  # Draw the squares on the board
    drawPieces(screen, gs.board)  # Draw the pieces on the board

# Function to draw the chessboard
def drawBoard(screen): 
    colors = [p.Color("wheat"), p.Color("saddlebrown")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Function to draw the pieces on the board
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # If the square is not empty
                screen.blit(IMAGES[piece], p.Rect(c * SQUARE_SIZE, r * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Main call
if  __name__ == "__main__":
    main()
