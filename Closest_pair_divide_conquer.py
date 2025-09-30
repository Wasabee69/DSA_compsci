import math

def distance(P, Q):
    return math.sqrt((P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2)

def brute_force(points):
    closest = float("inf")
    n = len(points)
    for i in range(1, n):
        for j in range(i):
            closest = min(closest, distance(points[i], points[j]))
    return closest

def closest_crossing(Y, split, delta):
    relevant = [p for p in Y if abs(split - p[0]) <= delta]
    n = len(relevant)
    if n < 2:
        return delta
    closest = delta
    for i in range(n):
        for j in range(i+1, min(i+8, n)):
            closest = min(closest, distance(relevant[i], relevant[j]))

    return closest

def closest_pair(X, Y):
    n = len(X)
    if n  <= 10:
        return brute_force(X)
    
    pivot = n // 2
    LX = X[:pivot]
    RX = X[pivot:]

    hsL = set(LX)
    LY = [p for p in Y if p in hsL]
    RY = [p for p in Y if p not in hsL]
    
    cL = closest_pair(LX, LY)
    cR = closest_pair(RX, RY)
    delta = min(cL, cR)
    cC = closest_crossing(Y, X[pivot][0], delta)

    return min(cL, cR, cC)



points = [(2,3), (12,30), (40,50), (5,1), (12,10), (3,4)]
X = sorted(points, key=lambda p: p[0])
Y = sorted(points, key=lambda p: p[1])
print(closest_pair(X, Y))
