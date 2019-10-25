def checksquare(board,x,y):
    d = {}
    for i in range(3):
        for j in range(3):
            num = board[x+i][y+j]
#                print(x+i, " ", y+j)
            if num != '.':
                if num not in d:
                    d[num] = 1
                else:
                    return False
    return True

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    d = {}
    for x in range(0,9,3):
        for y in range(0,9,3):
            result = self.checksquare(board, x, y)
            if result == False:
                return False

    for x in range(9):
        d = {}
        for y in range(9):
            num = board[x][y]
            if num != '.':
                if num not in d:
                    d[num] = 1
                else:
                    return False

    for y in range(9):
        d = {}
        for x in range(9):
            num = board[x][y]
            if num != '.':
                if num not in d:
                    d[num] = 1
                else:
                    return False

    return True
