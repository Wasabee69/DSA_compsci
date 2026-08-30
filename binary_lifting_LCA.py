##
import sys
input = sys.stdin.readline
n = int(input())
LOG = 32
parent = [[0]*LOG for _ in range(n)]
children = [[] for _ in range(n)]

for i in range(1, LOG):
    for node in range(n):
        parent[node][i] = parent[ parent[node][i-1] ][i-1]

depths = [0] * n
def dfs(node, d):
    depths[node] = d
    for v in children[node]:
        dfs(v, d+1)
dfs(0, 0)

def lift(node, k):
    for i in range(LOG-1, -1, -1):
        if k&(1<<i):
            node = parent[node][i]
    return node


def lca(a, b):
    da = depths[a]
    db = depths[b]
    
    if da > db:
        a = lift(a, da - db)
    elif da < db:
        b = lift(b, db - da)
    if a == b:
        return a

    for i in range(LOG-1, -1, -1):
        pa = parent[a][i]
        pb = parent[b][i]
        if pa != pb:
            a = pa
            b = pb

    start = parent[a][0]
    return start
