# bfs
from collections import deque
from collections import defaultdict


def bfs(start, end):
    a, b = start
    c, d = end
    queue = deque([(a, b, 0)])
    vis = {(a, b)}
    if matrix[a][b] != '.':
        for t in portal_list[matrix[a][b]]:
            tx1, ty1 = t
            if tx1 == a and ty1 == b:
                continue
            else:
                if (tx1, ty1) not in vis:
                    queue.append((tx1, ty1, 0))
                    vis.add((tx1, ty1))
    while queue:
        nx, ny, step = queue.popleft()
        if nx == c and ny == d:
            return step
        for i in range(4):
            tx, ty = nx + dic[i][0], ny + dic[i][1]
            if check(tx, ty) and (tx, ty) not in vis:
                queue.append((tx, ty, step + 1))
                vis.add((tx, ty))
                if matrix[tx][ty] != '.':
                    for t in portal_list[matrix[tx][ty]]:
                        tx1, ty1 = t
                        if tx1 == tx and ty1 == ty:
                            continue
                        else:
                            if (tx1, ty1) not in vis:
                                queue.append((tx1, ty1, step + 1))
                                vis.add((tx1, ty1))
    return -1


dic = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def check(x, y):
    if 0 <= x < m and 0 <= y < n and matrix[x][y] != '#':
        return True
    return False


m, n = 2, 4
matrix = ["..C.", "C.A."]
portal_list = defaultdict(list)
for i in range(m):
    for j in range(n):
        if matrix[i][j] != '#' and matrix[i][j] != '.':
            portal_list[matrix[i][j]].append((i, j))

print(bfs((0, 0), (m - 1, n - 1)))
