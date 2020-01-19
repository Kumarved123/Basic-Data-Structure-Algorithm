'''class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]


    def isSafe(self, c, colour, v):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    def graphColourUtil(self, m, colour, v):
        if  v == self.V:
            return True
        for c in range(1, m+1):
            if self.isSafe(c, colour, v):
                colour[v] = c
                if self.graphColourUtil( m, colour, (v+1)):
                    return True
                colour[v] = 0

    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == None:
            return False

        for c in colour:
            print(c, end= ' ')
        return True


# Driver Code
g = Graph(4)
g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3
g.graphColouring(m)'''


def isSafe(color,graph, c, v):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True


def color_util(graph, m, color, v):
    if v == len(graph):
        return True
    for c in range(1, m+1):
        if isSafe(color, graph, c, v):
            color[v] = c
            if color_util(graph, m, color, v+1) == True:
                return True
            color[v] = 0


def graphColouring(graph, m):
    color= [0]*V
    if color_util(graph, m, color, 0) == True:
        print(color)
    else:
        print('Not Possible to color the graph')


V=4
graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3
graphColouring(graph, m)