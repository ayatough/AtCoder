N = int(input())
A = [0] + list(map(int, input().split()))
AMAX = N

class BIT:
    def __init__(self, n):
        self.n = n+1
        self.bit = [0] * (n+1)

    def add(self, i, a):
        while i < self.n:
            self.bit[i] += a
            i += i & -i

    def update(self, i, a):
        v = self.sum(i) - self.sum(i - 1)
        self.add(i, a - v)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def bisect(self, a):
        if a <= 0:
            return 0
        i = 0
        r = 1
        while r < self.n:
            r <<= 1
        while r > 0:
            if i + r < self.n and self.bit[i + r] < a:
                a -= self.bit[i + r]
                i += r
            r >>= 1
        return i + 1

bit = BIT(AMAX)
ans = 0
for i in range(1, N+1):
    bit.update(A[i], i)
    ans += bit.sum(AMAX)

print(ans)
