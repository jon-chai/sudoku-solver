def solve(board):
    """
    Solves the sudoku board using backtracking algorithm
    param: board: a valid sudoku board, represented by a 2D int array
    return: whether solution is found
    """
    current = nextEmpty(board)
    if current[0] == -1 and current[1] == -1:
        return True
    row = current[0]
    col = current[1]
    #backtracking algorithm
    for i in range(1,10):
        board[row][col] = i
        if isValid(board):
            if solve(board):
                return True
        board[row][col] = 0

    return False

def isValid(board):
    """
    Determines if board is a valid sudoku board
    param: board: a sudoku board, represented by a 2D int array
    return: whether board is a valid one
    """
    numrows = len(board)
    numcols = len(board[0])
    #valid rows
    for row in range(numrows):
        for col in range(numcols):
            curr = board[row][col]
            if curr != 0 and board[row].count(curr) > 1:
                return False
    #valid cols
    for col in range(numcols):
        temp = []
        for row in range(numrows):
            curr = board[row][col]
            if curr != 0 and curr in temp:
                return False
            else:
                temp.append(curr)
    #valid box
    for i in range(3):
        for j in range(3):
            temp = []
            for row in range(3):
                for col in range(3):
                    temp.append(board[row + i*3][col + j*3])
            for check in range(1,10):
                if temp.count(check) > 1:
                    return False
    return True

def nextEmpty(board):
    """
    Finds row and col of next empty space on the board.
    param: board: a sudoku board, represented by a 2D int array
    return: (row, col) where row and col are ints representing coordinates of empty space
            (-1,-1) if board has no empty spaces
    """
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row,col)
    return (-1,-1)

def printBoard(board):
    """
    Prints the sudoku board to the console
    param: board: a sudoku board, represented by a 2D int array
    return: None
    """
    final = ""
    for row in board:
        final = final + str(row) + "\n"
    print(final)

def solvable(board):
    """
    Tells if a sudoku puzzle is valid and/or solvable, and solves 
    and prints board if possible
    param: board: a sudoku board, represented by a 2D int array
    return: None
    """
    orig = board
    result = solve(board)
    if result:
        print("Sudoku puzzle is solvable!")
        printBoard(board)
    else:
        if not isValid(orig):
            print("Sudoku puzzle is not valid! :(")
        else:
            print("Sudoku puzzle not solvable! :(")


board1 = [[1,2,3,4,5,6,7,8,9],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]

board2 = [[1,2,1,4,5,6,7,8,9],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]

board3 = [[1,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]]

board4 = [[1,2,0,0,0,0,0,0,0],
          [0,1,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,3,0,0,0,0,0],
          [0,0,0,0,0,3,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,4,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,4,0]]

board5 = [[5,1,6,8,4,9,7,3,2],
          [3,0,7,6,0,5,0,0,0],
          [8,0,9,7,0,0,0,6,5],
          [1,3,5,0,6,0,9,0,7],
          [4,7,2,5,9,1,0,0,6],
          [9,6,8,3,7,0,0,5,0],
          [2,5,3,1,8,6,0,7,4],
          [6,8,4,2,0,7,5,0,0],
          [7,9,1,0,5,0,6,0,8]]

if __name__ == "__main__":
    solvable(board1)
    solvable(board2)
    solvable(board3)
    solvable(board4)
    solvable(board5)


