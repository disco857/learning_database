class UnionFind:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for i in range(size)]

    def __str__(self):
        return str(self.parent)

    def find(self,p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self,p,q):
        root_p = self.find(p)
        root_q = self.find(q)
        if self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q
        elif self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = root_p
        else:
            self.parent[root_p] = root_q
            self.rank[root_q] += 1

    def is_connected(self,p,q):
        return self.find(p) == self.find(q)

    def num_of_sets(self):
        return sum(self.parent[i] == i for i in range(len(self.parent)))

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
n=len(isConnected)
uf = UnionFind(n)
for i in range(n):
    for j in range(i+1,n):
        if isConnected[i][j]==1:
            uf.union(i,j)
print(uf.num_of_sets())
