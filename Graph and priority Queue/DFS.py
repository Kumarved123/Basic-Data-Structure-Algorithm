from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def dfs_util(self, s, visited):
        visited[s] = True
        print(s, end = ' ')
        for i in self.graph[s]:
            if visited[i] == False:
                self.dfs_util(i, visited)

    def DFS(self, S):
        visited = [False]*len(self.graph)
        self.dfs_util(S, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)