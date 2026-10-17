####
class Fenwick:
    def __init__(self,  n):
        self.Tree = [0] * (n+2)
        self.n = n
    def update(self, i, delta):
        while i <= self.n+1:
            self.Tree[i] += delta
            i += i & -i
    def query(self, i):
        R = 0
        while i > 0:
            R += self.Tree[i]
            i -= i & -i
        return R
    def query_range(self, l, r):
        return self.query(r)-self.query(l-1)


class FenwickRange:
    def __init__(self,  n):
        self.T1 = [0] * (n+2)
        self.T2 = [0] * (n+2)
        self.n = n
    def u(self, tree, i, delta):
        i += 1
        while i <= self.n+1:
            tree[i] += delta
            i += i & -i

    def q(self, tree, i):
        i += 1
        R = 0
        while i > 0:
            R += tree[i]
            i -= i & -i
        return R
    
    def prefix(self, x):
        return (self.q(self.T1, x) * (x + 1)) - self.q(self.T2, x)
    
    def update(self, l, r, delta):
        self.u(self.T1, l, delta)
        self.u(self.T1, r + 1, -delta)

        self.u(self.T2, l, delta * l)
        self.u(self.T2, r + 1, -delta * (r+1))

    def query(self, l, r):
        return self.prefix(r) - self.prefix(l - 1)
    
