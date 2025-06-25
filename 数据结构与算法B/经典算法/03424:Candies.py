# Dijkstra算法
import heapq


def dijkstra(graph, start, end):
    dis = {i: float('inf') for i in range(n + 1)}
    dis[start] = 0
    queue = [(0, start)]
    heapq.heapify(queue)
    while queue:
        cur_dis, cur_node = heapq.heappop(queue)
        if cur_node == end:
            return cur_dis
        if cur_dis > dis[cur_node]:
            continue
        for neighbor, weight in graph[cur_node]:
            n_dis = cur_dis + weight
            if n_dis < dis[neighbor]:
                dis[neighbor] = n_dis
                heapq.heappush(queue, (n_dis, neighbor))
    return -1


n, m = map(int, input().split())
kids = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    kids[a].append((b, c))

ans = dijkstra(kids, 1, n)
print(ans)
