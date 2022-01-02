def initTable(board):

    # init the pawns
    for i in range(8):
        board[1][i] = 'Pawn'
        board[6][i] = 'Pawn'

    # init the rooks
    board[0][0] = 'Rook'
    board[0][7] = 'Rook'
    board[7][0] = 'Rook'
    board[7][7] = 'Rook'

    # init the knights
    board[0][1] = 'Knight'
    board[0][6] = 'Knight'
    board[7][1] = 'Knight'
    board[7][6] = 'Knight'

    # init the bishops
    board[0][2] = 'Bishop'
    board[0][5] = 'Bishop'
    board[7][2] = 'Bishop'
    board[7][5] = 'Bishop'

    # init the queen
    board[0][3] = 'Queen'
    board[7][3] = 'Queen'
    
    # init the king
    board[0][4] = 'King'
    board[7][4] = 'King'


def printTable(board):
    for i in range(8):
        print(board[i])


def PawnMove(board, start, end):
    # check if the move is valid
    if isValidPawnMove(board, start, end):
        # move the piece
        board[end[0]][end[1]] = board[start[0]][start[1]]
        board[start[0]][start[1]] = ' '
    else:
        print('Invalid move!')

def isValidPawnMove(board, start, end):
    # check if the move is valid
    if board[end[0]][end[1]] != ' ':
        return False
    if start[0] == 1 and start[1] == end[1]:
        return True
    if start[0] == 6 and start[1] == end[1]:
        return True
    if start[0] == end[0] - 1 and start[1] == end[1]:
        return True
    if start[0] == end[0] + 1 and start[1] == end[1]:
        return True
    return False


def KnightMove(board, start, end):
    # check if the move is valid
    if isValidKnightMove(board, start, end):
        # move the piece
        board[end[0]][end[1]] = board[start[0]][start[1]]
        board[start[0]][start[1]] = ' '
    else:
        print('Invalid move!')

def isValidKnightMove(board, start, end):
    # check if the move is valid
    if board[end[0]][end[1]] != ' ':
        return False
    if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
        return True
    if abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2:
        return True
    return False

def BishopMove(board, start, end):
    # check if the move is valid
    if isValidBishopMove(board, start, end):
        # move the piece
        board[end[0]][end[1]] = board[start[0]][start[1]]
        board[start[0]][start[1]] = ' '
    else:
        print('Invalid move!')

def isValidBishopMove(board, start, end):
    # check if the move is valid
    if board[end[0]][end[1]] != ' ':
        return False
    if abs(start[0] - end[0]) == abs(start[1] - end[1]):
        return True
    return False

def RookMove(board, start, end):
    # check if the move is valid
    if isValidRookMove(board, start, end):
        # move the piece
        board[end[0]][end[1]] = board[start[0]][start[1]]
        board[start[0]][start[1]] = ' '
    else:
        print('Invalid move!')

def isValidRookMove(board, start, end):
    # check if the move is valid
    if board[end[0]][end[1]] != ' ':
        return False
    if start[0] == end[0] or start[1] == end[1]:
        return True
    return False

def QueenMove(board, start, end):
    # check if the move is valid
    if isValidQueenMove(board, start, end):
        # move the piece
        board[end[0]][end[1]] = board[start[0]][start[1]]
        board[start[0]][start[1]] = ' '
    else:
        print('Invalid move!')

def isValidQueenMove(board, start, end):
    # check if the move is valid
    if board[end[0]][end[1]] != ' ':
        return False
    if start[0] == end[0] or start[1] == end[1]:
        return True
    if abs(start[0] - end[0]) == abs(start[1] - end[1]):
        return True
    return False

def KingMove(board, start, end):
    # check if the move is valid
    if isValidKingMove(board, start, end):
        # move the piece
        board[end[0]][end[1]] = board[start[0]][start[1]]
        board[start[0]][start[1]] = ' '
    else:
        print('Invalid move!')

def isValidKingMove(board, start, end):
    # check if the move is valid
    if board[end[0]][end[1]] != ' ':
        return False
    if abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1:
        return True
    return False

def MovePiece(board, start, end):
    if board[start[0]][start[1]] == 'Pawn':
        PawnMove(board, start, end)
    elif board[start[0]][start[1]] == 'Rook':
        RookMove(board, start, end)
        Castling(board, start, end)
    elif board[start[0]][start[1]] == 'Knight':
        KingMove(board, start, end)
    elif board[start[0]][start[1]] == 'Bishop':
        BishopMove(board, start, end)
    elif board[start[0]][start[1]] == 'Queen':
        QueenMove(board, start, end)
    elif board[start[0]][start[1]] == 'King':
        KingMove(board, start, end)
        Castling(board, start, end)
    else:
        return None

    
def Castling(board, start, end):
    if board[start[0]][start[1]] == 'King':
        if start[1] == 4 and end[1] == 6:
            board[start[0]][start[1]] = ' '
            board[start[0]][start[1] + 1] = 'Rook'
            board[start[0]][start[1] + 2] = 'King'
        elif start[1] == 4 and end[1] == 2:
            board[start[0]][start[1]] = ' '
            board[start[0]][start[1] - 1] = 'Rook'
            board[start[0]][start[1] - 2] = 'King'
    else:
        return None

def findBestMove(board):
    bestMove = None
    bestScore = -9999
    for i in range(8):
        for j in range(8):
            if board[i][j] != ' ':
                for k in range(8):
                    for l in range(8):
                        if isValidMove(board, (i, j), (k, l)):
                            newBoard = deepcopy(board)
                            MovePiece(newBoard, (i, j), (k, l))
                            score = evaluateBoard(newBoard)
                            if score > bestScore:
                                bestScore = score
                                bestMove = (i, j), (k, l)
    return bestMove


def isValidMove(board, start, end):
    if board[start[0]][start[1]] == 'Pawn':
        return isValidPawnMove(board, start, end)
    elif board[start[0]][start[1]] == 'Knight':
        return isValidKnightMove(board, start, end)
    elif board[start[0]][start[1]] == 'Bishop':
        return isValidBishopMove(board, start, end)
    elif board[start[0]][start[1]] == 'Rook':
        return isValidRookMove(board, start, end)
    elif board[start[0]][start[1]] == 'Queen':
        return isValidQueenMove(board, start, end)
    elif board[start[0]][start[1]] == 'King':
        return isValidKingMove(board, start, end)
    else:
        return False

def deepcopy(board):
    newBoard = []
    for i in range(8):
        newBoard.append([])
        for j in range(8):
            newBoard[i].append(board[i][j])
    return newBoard

def evaluateBoard(board):
    score = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'Pawn':
                score += 1
            elif board[i][j] == 'Knight':
                score += 3
            elif board[i][j] == 'Bishop':
                score += 3
            elif board[i][j] == 'Rook':
                score += 5
            elif board[i][j] == 'Queen':
                score += 9
            elif board[i][j] == 'King':
                score += 100
    return score

def isGameCanPlayable(board):
    if isCheck(board):
        if isCheckMate(board):
            return False
    return True

def isCheck(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] != ' ':
                for k in range(8):
                    for l in range(8):
                        if isValidMove(board, (i, j), (k, l)):
                            newBoard = deepcopy(board)
                            MovePiece(newBoard, (i, j), (k, l))
                            if isCheck(newBoard):
                                return True
    return False

def isCheckMate(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] != ' ':
                for k in range(8):
                    for l in range(8):
                        if isValidMove(board, (i, j), (k, l)):
                            newBoard = deepcopy(board)
                            MovePiece(newBoard, (i, j), (k, l))
                            if not isCheck(newBoard):
                                return False
    return True


def findCheckMateMove(board):
    bestMove = None
    bestScore = -9999
    for i in range(8):
        for j in range(8):
            if board[i][j] != ' ':
                for k in range(8):
                    for l in range(8):
                        if isValidMove(board, (i, j), (k, l)):
                            newBoard = deepcopy(board)
                            MovePiece(newBoard, (i, j), (k, l))
                            score = evaluateBoard(newBoard)
                            if score > bestScore:
                                bestScore = score
                                bestMove = (i, j), (k, l)
    return bestMove


def findAllPosibbleMoves(board):
    possibleMoves = []
    for i in range(8):
        for j in range(8):
            if board[i][j] != ' ':
                for k in range(8):
                    for l in range(8):
                        if isValidMove(board, (i, j), (k, l)):
                            possibleMoves.append(((i, j), (k, l)))
    return possibleMoves