import random
import itertools
numbers = [1,2,3,4,5,6,7,8,9]

def attempt_board(m=3):
    """Make one attempt to generate a filled m**2 x m**2 Sudoku board,
    returning the board if successful, or None if not.

    """
    n = m**2
    numbers = list(range(1, n + 1))
    board = [[None for _ in range(n)] for _ in range(n)]
    for i, j in itertools.product(range(n), repeat=2):
        i0, j0 = i - i % m, j - j % m # origin of mxm block
        random.shuffle(numbers)
        for x in numbers:
            if (x not in board[i]                     # row
                and all(row[j] != x for row in board) # column
                and all(x not in row[j0:j0+m]         # block
                        for row in board[i0:i])):
                board[i][j] = x
                break
        else:
            # No number is valid in this cell.
            return None
    return board

def make_board(m=3):
    """Return a random filled m**2 x m**2 Sudoku board."""
    n = m**2
    board = [[None for _ in range(n)] for _ in range(n)]

    def search(c=0):
        "Recursively search for a solution starting at position c."
        i, j = divmod(c, n)
        i0, j0 = i - i % m, j - j % m # Origin of mxm block
        numbers = list(range(1, n + 1))
        random.shuffle(numbers)
        for x in numbers:
            if (x not in board[i]                     # row
                and all(row[j] != x for row in board) # column
                and all(x not in row[j0:j0+m]         # block
                        for row in board[i0:i])): 
                board[i][j] = x
                if c + 1 >= n**2 or search(c + 1):
                    return board
        else:
            # No number is valid in this cell: backtrack and try again.
            board[i][j] = None
            return None

    return search()

def printBoard(board):
    spacer = "++---+---+---++---+---+---++---+---+---++"
    print (spacer.replace('-','='))
    for i,line in enumerate(board):
        print ("|| {} | {} | {} || {} | {} | {} || {} | {} | {} ||".format(
                    line[0][0] if line[0][1] else ' ',
                    line[1][0] if line[1][1] else ' ',
                    line[2][0] if line[2][1] else ' ',
                    line[3][0] if line[3][1] else ' ',
                    line[4][0] if line[4][1] else ' ',
                    line[5][0] if line[5][1] else ' ',
                    line[6][0] if line[6][1] else ' ',
                    line[7][0] if line[7][1] else ' ',
                    line[8][0] if line[8][1] else ' ',))
        if (i+1) % 3 == 0: print(spacer.replace('-','='))
        else: print(spacer)

print(make_board())
