def issafe(maze, x, y):
    N = len(maze)
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
    return False

def solve(maze, x, y, sol):
    n = len(maze)
    if x == n-1 and y == n-1:
        sol[x][y] = 1
        return True

    if issafe(maze, x, y, ):
        sol[x][y] = 1
        if solve(maze, x+1, y, sol) == True:
            return True
        if solve(maze, x, y+1, sol) == True:
            return True
        sol[x][y] = 0
        return False


def Print(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end= ' ')
        print()


def solveMaze(maze):
    x = y = 0
    n = len(maze)
    sol = [[0 for i in range(n)] for i in range(n)]
    solve(maze, x, y, sol)
    Print(sol)

if __name__ ==  "__main__" :
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]

    solveMaze(maze)

