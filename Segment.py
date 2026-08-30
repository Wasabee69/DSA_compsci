###


class Segment:
    def __init__(self, n, nums):
        self.Tree = [0] * n + nums
        self.n = n
    def construct(self):
        for i in range(self.n - 1, 0, -1):
            self.Tree[i] = self.Tree[i<<1] + self.Tree[(i<<1) + 1]

    def query(self, left, right):
        left += n
        right += n - 1
        res = 0
        while left <= right:
            if left&1:
                res += self.Tree[left]
                left += 1
            if right&1 == 0:
                res += self.Tree[right]
                right -= 1
            left>>=1
            right>>=1
        return res
    
    def update(self, i, x):
        node = i + self.n
        self.Tree[node] = x
        node = self.parent(node)
        while node > 0:
            self.Tree[node] = self.Tree[node<<1] +self.Tree[(node<<1)+1]
            node>>=1

n = 100
first_n = Segment(n, list(range(n+1)))
first_n.construct()
print(first_n.Tree)
print(first_n.query(0, 4))
print(first_n.query(0, 5))
print(first_n.query(0, 6))
print(first_n.query(0, 7))
print(first_n.query(0, 8))
print(first_n.query(0, 50))