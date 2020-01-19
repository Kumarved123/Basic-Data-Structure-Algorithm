def is_safe(matrix, x, y, val):
    for i in range(9):
        if matrix[x][i] == val:
            return False
    for i in range(9):
        if matrix[i][y] == val:
            return False
    box_X = 3*(x//3)
    box_Y = 3*(y//3)
    for i in range(box_X, box_X +3):
        for j in range(box_Y, box_Y + 3):
            if matrix[i][y] == val:
                return False


def mprint(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end = ' ')
        print()

def find_space(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[j][i]==0:
                return False
            break
    return True

def solve(matrix):
    pass



matrix = [[3,0,6,5,0,8,4,0,0],
          [5,2,0,0,0,0,0,0,0],
          [0,8,7,0,0,0,0,3,1],
          [0,0,3,0,1,0,0,8,0],
          [9,0,0,8,6,3,0,0,5],
          [0,5,0,0,9,0,6,0,0],
          [1,3,0,0,0,0,2,5,0],
          [0,0,0,0,0,0,0,7,4],
          [0,0,5,2,0,6,3,0,0]]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[i][j] = 9
print(find_space(matrix))

