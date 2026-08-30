###
import sys
from math import cos, sin, atan2 as arctan, sqrt
from collections import deque
input = sys.stdin.readline
EPS = 1e-9
class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(A, B):
        return Vec(A.x + B.x, A.y + B.y)
    def __sub__(A, B):
        return Vec(A.x - B.x, A.y - B.y)
    def __mul__(A, c):
        return Vec(A.x * c, A.y * c)
    def dot(A, B):
        return A.x * B.x + A.y * B.y
    def cross(A, B):
        return A.x * B.y - A.y * B.x
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.P = Vec(x1, y1)
        self.U = Vec(x2 - x1, y2 - y1)

def intersect(line1, line2):
    P1, P2 = line1.P, line2.P
    U1, U2 = line1.U, line2.U
    den = Vec.cross(U1, U2)
    if abs(den) <= EPS: return None
    t = Vec.cross(P2 - P1, U2) / den
    return P1 + U1 * t

def outside(X, L):
    return Vec.cross(X - L.P, L.U) < 0
def leftof(A, B):
    return Vec.cross(A, B) >= 0
def same_dir(A, B):
    return abs(Vec.cross(A.U, B.U)) <= 0 and Vec.dot(A.U, B.U) > 0
def dist(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def hull(lines):
    lines = sorted(lines, key = lambda L: arctan(L.U.y, L.U.x))
    Q = deque()
    for L in lines:
        while len(Q) > 1 and outside(intersect(Q[-1], Q[-2]), L):
            Q.pop()
        while len(Q) > 1 and outside(intersect(Q[0], Q[1]), L):
            Q.popleft()
        if Q and same_dir(Q[-1], L):
            if outside(Q[-1].P, L):
                Q.pop()
            else: continue
        Q.append(L)
    ## final cleanup
    while len(Q) > 2 and outside(intersect(Q[-2], Q[-1]), Q[0]):
        Q.pop()
    while len(Q) > 2 and outside(intersect(Q[0], Q[1]), Q[-1]):
        Q.popleft()
    # vertices in CCW order:
    ans = []
    for i in range(len(Q)):
        I = intersect(Q[i-1], Q[i])
        if I is None: return []
        ans.append((I.x, I.y))
    return ans

lines = []
Hull = hull(lines)