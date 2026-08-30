###
import sys
input = sys.stdin.readline
n = int(input())
INF = 10**9

graph = [[] for _ in range(n)]
dp = [[INF] * n for _ in range(1<<n)]

for u in range(n):
    dp[1<<u][u] = 0

for subset in range(1<<n):
    for u in range(n):
        if subset & (1<<u):
            child = (subset ^ (1<<u))
            for v, w in graph[u]:
                if child & (1<<v) and dp[child][v] != INF:
                    dp[subset][u] = min(dp[subset][u], dp[child][v] + w)

print(min(dp[(1<<n)-1]))
