N = int(input())
X = list(map(int, input().split()))
XMAX = X[-1]

class BIT_RAQ:
    def __init__(self, n):
        self.n = n+1
        self.bit = [[0] * (n+1) for _ in range(2)]

    def add(self, l, r, a):
        """ [l, r)
        """
        self._add(0, l, a)
        self._add(0, r, -a)
        self._add(1, l, -(l-1)*a)
        self._add(1, r, (r-1)*a)

    def _add(self, p, i, a):
        while i < self.n:
            self.bit[p][i] += a
            i += i & -i

    def _update(self, p, i, a):
        v = self.sum(i) - self.sum(i - 1)
        self.add(p, i, a - v)

    def sum(self, i):
        return self._sum(0, i) * i + self._sum(1, i)

    def _sum(self, p, i):
        s = 0
        while i > 0:
            s += self.bit[p][i]
            i -= i & -i
        return s


bit = BIT_RAQ(XMAX)

Q = int(input())
for _ in range(Q):
    T, G = map(int, input().split())

