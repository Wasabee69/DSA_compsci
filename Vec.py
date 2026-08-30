####
import sys, math
from math import cos, sin, atan2 as arctan, sqrt
class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.theta = arctan(self.y, self.x)
        self.modulus = sqrt(x**2 + y**2)
    def __add__(A, B):
        return Vec(A.x + B.x, A.y + B.y)
    def __sub__(A, B):
        return Vec(A.x - B.x, A.y - B.y)
    def __mul__(A, c):
        return Vec(A.x * c, A.y * c)
    def __lt__(A, B):
        # når vi sorterer
        # for [A < B] : Gir counter-clockwise, siden vinkel er mellom [-pi, pi], MINST vinkel kommer først, og STØRST vinkel kommer sist, . A kommer før B.
        # så vi går i en sirkel fra -pi -> +pi.
        # Men vi ønsker det motsatte for clockwise. La B komme før A. så A.theta > B.theta..
        # Da går i vi i en sirkel fra +pi -> -pi.... Størst til minst, med klokken
        return A.theta > B.theta
    def rotate(A, delta):
        nx = A.x * cos(delta) - A.y * sin(delta)
        ny = A.x * sin(delta) + A.y * cos(delta)
        return Vec(nx, ny)
    def shoelace(XY):
        n = len(XY)
        area = 0
        for i in range(n):
            x0=XY[i-1].x;y0=XY[i-1].y
            x1=XY[i].x;y1=XY[i].y
            area += x0*y1 - y0*x1
        return area / 2.0
    
    def area(vertices):
        return abs(Vec.shoelace(vertices))
    def orient(a, b, c):
        return Vec.cross(b - a, c - a)
    def dot(A, B):
        return A.x * B.x + A.y * B.y
    def cross(A, B):
        return A.x * B.y - A.y * B.x
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.PQ = [Vec(x1, y1), Vec(x2, y2)]
    def sgn(k, l):
        return k * l < 0
    def intersect(line1, line2):
        (a, b), (c, d) = line1.PQ, line2.PQ
        # a.x + t * (b.x - a.x) = c.x + u * (d.x - c.x) OG  a.y + t * (b.y - a.y) = c.y + u * (d.y - c.y)
        # a.x - c.x = u * (d.x - c.x) - t * (b.x - a.x) OG a.y - c.y = u * (d.y - c.y) - t * (b.y - a.y)
        # Så et likningssystem -> ut = [u, t], A = [[d.x-c.x, -b.x + a.x : a.x - c.x],
        #                                           [d.y-c.y, -b.y + a.y : a.y - c.y]]
        ## løser for u og t; Cramers-regel, trenger kun en av dem-> x_i = det A_i(b) / det(A)
        # t = x_2 = ( (d.x-c.x) * (a.y - c.y) - (a.x - c.x) * (d.y-c.y) ) / ( (d.x-c.x) * (-b.y + a.y) - (-b.x + a.x) * (d.y-c.y) )
        oa = Vec.orient(c, d, a)
        ob = Vec.orient(c, d, b)
        oc = Vec.orient(a, b, c)
        od = Vec.orient(a, b, d)
        if Line.sgn(oa, ob) and Line.sgn(oc, od):
            t = ( (d.x-c.x) * (a.y - c.y) - (a.x - c.x) * (d.y-c.y) ) / ( (d.x-c.x) * (-b.y + a.y) - (-b.x + a.x) * (d.y-c.y) )
            return a + (b - a) * t # returnerer et punkt på linjen til a->b
        return None

# Clockwise sortering
P = [Vec(2, 3), Vec(4, 5), Vec(1, 5), Vec(5, 1), Vec(0, 2), Vec(4, 0)]
c = Vec(4, 1)
Q = sorted([(v - c, v) for v in P])
P_sorted = [v for _, v in Q]


class Line:
    def __init__(self, m, b):
        self.m = m
        self.b = b
    def value(self, x):
        return self.m * x + self.b
    
def intersect_x(L1, L2):
    return (L2.b - L1.b) / (L1.m - L2.m)


def envelope(lines, so_key):
    lines = sorted(lines, key=lambda L: (L.m, L.b))
    filtered = []
    for L in lines:
        if filtered and L.m == filtered[-1].m:
            if so_key(L.b, filtered[-1].b):
                filtered[-1] = L
        else:
            filtered.append(L)


    hull = []
    for L in filtered:
        while len(hull) >= 2:
            x12 = intersect_x(hull[-2], hull[-1])
            x23 = intersect_x(hull[-1], L)
            if x12 >= x23:
                hull.pop()
            else:
                break
        hull.append(L)
    return hull


lines = []
upper_envelope = envelope(lines, lambda x, y: x > y)
lower_envelope = envelope(lines, lambda x, y: x < y)

