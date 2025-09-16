####
import heapq
def prims(edges, n):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    heap = [(w, v) for v, w in graph[0]]
    heapq.heapify(heap)
    S = [False] * n
    S[0] = True
    def update(node):
        S[node] = True
        for nei, edge_weight in graph[node]:
            if S[nei] == False:
                heapq.heappush(heap, (edge_weight, nei))
                
    res = 0
    while heap:
        w, v = heapq.heappop(heap)
        if S[v] == False:
            update(v)
            res += w

    return res

print(prims(edges = [(0, 1, 10),(0, 2, 6),(0, 3, 5),(1, 3, 15),(2, 3, 4)],n = 4))

