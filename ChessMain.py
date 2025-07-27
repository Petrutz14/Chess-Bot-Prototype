import pygame as p
import ChessEngine

#Initializing constants
WIDTH = HEIGHT = 512
DIMENSION = 8  # Chessboard is 8x8
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # For animations
IMAGES = {}

#Image loading function
def loadImages():
    pieces = ['bK', 'bN', 'bB', 'bR', 'bQ', 'bP', 'wK', 'wN', 'wB', 'wR', 'wQ', 'wP']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f'images/{piece}.png'), (SQUARE_SIZE, SQUARE_SIZE))

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs= ChessEngine.GameState()
    loadImages();
    running = True;
    #Game loop
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

#Game state drawing function
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
    pass

#Main call
if  __name__ == "__main__":
    main()