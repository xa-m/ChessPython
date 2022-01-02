import Game

# create a chess board
board = [[' ' for i in range(8)] for j in range(8)]
# print the board

# game loop

Game.initTable(board)

print("Example Move: \nStart: 6 0 \nEnd: 4 0\n\n")

moveStart = input('Enter Start: ').strip().split(" ")
moveEnd = input('Enter End: ').split(" ")

Game.MovePiece(board, (int(moveStart[0]), int(moveStart[1])), (int(moveEnd[0]), int(moveEnd[1])))

Game.printTable(board)