from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printAllPathsutil(self, s, d, visited, path):
        visited[s] = True
        path.append(s)
        if s == d:
            print(path)
        else:
            for i in self.graph[s]:
                if visited[i] == False:
                    self.printAllPathsutil(i, d, visited, path)
        path.pop()
        visited[s] == False

    def printAllPaths(self, s, d):
        visited = [False]*self.V
        path = []
        self.printAllPathsutil(s, d, visited, path)

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

s = 2;
d = 3
print("Following are all different paths from %d to %d :" % (s, d))
g.printAllPaths(s, d)