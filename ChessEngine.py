class GameState():
    def __init__(self):
    # Initialize the game state with a standard chess board setup
    # First character - color; Second character - piece type; "--" - Empty space
        self.board=[
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True # Boolean to track whose turn it is
        self.moveLog = []  # List to keep track of moves made

    # Function to make a move on the board
    def makeMove(self, move):
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.moveLog.append(move) #Log the move
            self.whiteToMove = not self.whiteToMove  # Switch turns 
    # Function to undo the last move
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board [move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove  # Switch turns back
    # Function to get all valid moves for the current player
    def getValidMoves(self):
        return self.getAllPossibleMoves()

    # Function to get all possible moves for the current player
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                piece = self.board[r][c]
                if piece != "--":
                    color = piece[0]
                    type = piece[1]
                    if (color == 'w' and self.whiteToMove) or (color == 'b' and not self.whiteToMove):
                        if type == 'P':
                            self.getPawnMoves(r, c, moves)
                        elif type == 'R':
                            self.getRookMoves(r, c, moves)
                        elif type == 'N':
                            self.getKnightMoves(r, c, moves)
                        elif type == 'B':
                            self.getBishopMoves(r, c, moves)
                        elif type == 'Q':
                            self.getQueenMoves(r, c, moves)
                        elif type == 'K':
                            self.getKingMoves(r, c, moves)
        return moves
    # Get moves for each piece type
    def getPawnMoves(self, r, c, moves):
        if self.whiteToMove:
            #One move forward
            if self.board[r-1][c] == "--":
                moves.append(Move((r, c), (r-1, c), self.board))
                if r == 6 and self.board[r-2][c] == "--":  # Two moves forward
                    moves.append(Move((r, c), (r-2, c), self.board))
            if c-1 > 0 and self.board[r-1][c-1][0] == 'b':  # Capture left
                moves.append(Move((r, c), (r-1, c-1), self.board))
            if c+1 < 7 and self.board[r-1][c+1][0] == 'b':  # Capture right
                moves.append(Move((r, c), (r-1, c+1), self.board))
        else:
            #Black pawn moves
            if self.board[r+1][c] == "--":
                moves.append(Move((r, c), (r+1, c), self.board))
                if r == 1 and self.board[r+2][c] == "--":  # Two moves forward
                    moves.append(Move((r, c), (r+2, c), self.board))
            if c-1 > 0 and self.board[r+1][c-1][0] == 'w':  # Capture left
                moves.append(Move((r, c), (r+1, c-1), self.board))
            if c+1 < 7 and self.board[r+1][c+1][0] == 'w':  # Capture right
                moves.append(Move((r, c), (r+1, c+1), self.board))

    def getRookMoves(self, r, c, moves):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        enemyColor = 'b' if self.whiteToMove else 'w'
        for dr in directions:
            for i in range(1, 8):
                endRow = r + dr[0] * i
                endCol = c + dr[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    if self.board[endRow][endCol] == "--":
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                    elif self.board[endRow][endCol][0] == enemyColor:
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                        break    
                    else:
                        break
                else:
                    break # Out of bounds
    def getKnightMoves(self, r, c, moves):
        knightMoves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        enemyColor = 'b' if self.whiteToMove else 'w'
        for move in knightMoves:
            endRow = r + move[0]
            endCol = c + move[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                if self.board[endRow][endCol] == "--":
                    moves.append(Move((r, c), (endRow, endCol), self.board))
                elif self.board[endRow][endCol][0] == enemyColor:
                    moves.append(Move((r, c), (endRow, endCol), self.board))
        
    def getBishopMoves(self, r, c, moves):
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        enemyColor = 'b' if self.whiteToMove else 'w'
        for dr in directions:
            for i in range(1, 8):
                endRow = r + dr[0] * i
                endCol = c + dr[1] * i
                if 0 <= endRow < 8 and 0 <= endCol < 8:
                    if self.board[endRow][endCol] == "--":
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                    elif self.board[endRow][endCol][0] == enemyColor:
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                        break    
                    else:
                        break
                else:
                    break
    def getQueenMoves(self, r, c, moves):
        self.getRookMoves(r, c, moves)
        self.getBishopMoves(r, c, moves)
    def getKingMoves(self, r, c, moves):
        kingMoves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        enemyColor = 'b' if self.whiteToMove else 'w'
        for move in kingMoves:
            endRow = r + move[0]
            endCol = c + move[1]
            if 0 <= endRow < 8 and 0 <= endCol < 8:
                if self.board[endRow][endCol] == "--":
                    moves.append(Move((r, c), (endRow, endCol), self.board))
                elif self.board[endRow][endCol][0] == enemyColor:
                    moves.append(Move((r, c), (endRow, endCol), self.board))

        
#--------------------------------------------------------------------------------------------------------------
# Function to make a move on the board
class Move(): 
    # Mapping ranks and files to rows and columns
    ranksToRows = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    # Constructor for the Move class
    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID= self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    # Convert the move to standard chess notation
    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)
    def getRankFile(self,r,c):
        return self.colsToFiles[c]+self.rowsToRanks[r]
    
     
