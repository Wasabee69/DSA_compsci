###
import sys
input = sys.stdin.readline

def leftof(a, b, P):
    ax, ay = a
    bx, by = b
    Px, Py = P
    aP = Px-ax, Py-ay
    ab = bx-ax, by-ay
    # Om kryssprodukt er > 0 er punktet P til venstre for vektorern a -> b: ab
    return cross(ab, aP) > 0

def cross(A, B):
    ax, ay = A
    bx, by = B
    return ax * by - ay * bx

def graham(points):
    points = sorted(set(points))
    S, hull = [], [] # S is a stack of points
    # Lower hull
    for P in points:
        while len(S) >= 2 and not leftof(S[-2], S[-1], P):
            S.pop()
        S.append(P)
    hull += S
    # Upper hull
    S = []
    for P in reversed(points):
        while len(S) >= 2 and not leftof(S[-2], S[-1], P):
            S.pop()
        S.append(P)
    hull += S[1:-1] # ignore endpoints
    return hull