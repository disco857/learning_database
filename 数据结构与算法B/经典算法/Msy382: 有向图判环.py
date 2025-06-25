from collections import deque
class Vertex:
    def __init__(self,key):
        self.key = key
        self.neighbors = []

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        if key not in self.vertices:
            self.vertices[key] = Vertex(key)

    def add_edge(self, key1, key2):
        self.add_vertex(key1)
        self.add_vertex(key2)
        self.vertices[key1].neighbors.append(self.vertices[key2])

def kahn(graph):
    in_degree = {key: 0 for key in graph.vertices}
    for key in graph.vertices:
        for neighbor in graph.vertices[key].neighbors:
            in_degree[neighbor.key] += 1

    queue = deque([key for key in in_degree if in_degree[key] == 0])
    topo_order = []
    while queue:
        vertex = queue.popleft()
        for neighbor in graph.vertices[vertex].neighbors:
            in_degree[neighbor.key] -= 1
            if in_degree[neighbor.key] == 0:
                queue.append(neighbor.key)
        topo_order.append(vertex)

    if len(topo_order) != len(graph.vertices):
        return True
    else:
        return False

n,m = map(int, input().split())
gh = Graph()
for i in range(n):
    gh.add_vertex(i)

for _ in range(m):
    a,b = map(int, input().split())
    gh.add_edge(a,b)

if kahn(gh):
    print('Yes')
else:
    print('No')