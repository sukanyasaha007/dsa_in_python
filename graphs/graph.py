class Graph:
    def __init__(self, gdict= {}) :
        self.gdict= gdict
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    def bfs(self, startV):
        visited= [startV]
        queue= [startV]
        while queue:
            currentV= queue.pop(0)
            print(currentV)
            for adjV in self.gdict[currentV]:
                if not adjV in visited:
                    visited.append(adjV)
                    queue.append(adjV)

g= Graph({'A': ['B'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C']})
g.addEdge('A', 'C')
g.addEdge('A', 'D')
g.addEdge('D', 'A')
print(g.gdict)
g.bfs('B')