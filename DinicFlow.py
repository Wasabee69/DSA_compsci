###
import sys
from collections import deque, defaultdict
INF = 10**9+7

class DinicFlow:
    def __init__(self, n):
        self.graph = [[] for _ in range(n)]
        self.levels = [-1]*n
        self.next = [0] * n
        self.n = n

    def addEdge(self, u, v, w):
        self.graph[u].append( [v, w, len(self.graph[v])] )
        self.graph[v].append( [u, 0, len(self.graph[u])-1] )

    def bfs(self, s, t):
        q = deque([s])
        self.levels = [-1]*self.n
        self.levels[s] = 0
        while q:
            u = q.popleft()
            for v, capacity, idx in self.graph[u]:
                if self.levels[v] != -1 or capacity <= 0: continue
                self.levels[v] = self.levels[u] + 1
                q.append(v)
        return self.levels[t] != -1

    def push(self, u, t, try_push):
        if u == t or try_push == 0: return try_push

        while (idxUV := self.next[u]) < len(self.graph[u]):
            v, capacity, idxVU = self.graph[u][idxUV]

            if capacity > 0 and self.levels[u]+1 == self.levels[v]:

                b = self.push(v, t, min(try_push, capacity))
                if b:
                    self.graph[u][idxUV][1] -= b
                    self.graph[v][idxVU][1] += b
                    return b

            self.next[u] += 1
        return 0
    def maxFlow(self, s, t):
        flow = 0
        while P := self.bfs(s, t):
            self.next = [0] * self.n
            while b := self.push(s, t, INF):
                flow += b
        return flow