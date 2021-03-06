#Dijkstra’s shortest path algorithm
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def findmin(self, distance, visited):
        min = float('inf')
        for v in range(self.V):
            if distance[v] < min and visited[v] == False:
                min = distance[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        distance = [float('inf')]*self.V
        distance[src] = 0
        visited = [False]*self.V
        for k in range(self.V):
            u = self.findmin(distance, visited)
            visited[u] = True
            for i in range(self.V):
                if self.graph[u][i] > 0 and visited[i] == False and distance[i] > distance[u]+ self.graph[u][i]:
                    distance[i] = distance[u]+ self.graph[u][i]
        self.printSolution(distance)

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
g.dijkstra(0)