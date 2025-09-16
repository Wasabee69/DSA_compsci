###
def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])
    roots = list(range(n))
    rank = [0] * n

    def union_find(node):
        if roots[node] != node:
            roots[node] = union_find(roots[node])
        return roots[node]
    def unionize(u, v):
        if rank[u] >= rank[v]:
            roots[v] = roots[u]
            if rank[u] == rank[v]:
                rank[u] += 1
        else:
            roots[u] = roots[v]
    res = 0
    for u, v, w in edges:
        r1, r2 = union_find(u), union_find(v)
        if r1 != r2:
            res += w
            unionize(r1, r2)
    return res

print(kruskal(edges = [(0, 1, 10),(0, 2, 6),(0, 3, 5),(1, 3, 15),(2, 3, 4)],n = 4))

