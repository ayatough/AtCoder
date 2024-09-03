N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
B2 = [b > 1 for b in B]
Q = int(input())
ans = []

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

bA = BIT(N)
bB = BIT(N)
bB2 = BIT(N)

for i in range(N):
    bA.update(i+1, A[i])
    bB.update(i+1, B[i])
    bB2.update(i+1, B2[i])

for _ in range(Q):
    args = list(map(int, input().split()))
    op = args[0]
    if op == 1:
        i, x = args[1:]
        bA.add(i, x - A[i-1])
        A[i-1] = x
    elif op == 2:
        i, x = args[1:]
        bB.add(i, x - B[i-1])
        B[i-1] = x
        bB2.add(i, (x > 1) - B2[i-1])
        B2[i-1] = x > 1
    else:
        l, r = args[1:]
        v = A[l-1]
        i = l+1
        while i <= r:
            base = bB2.sum(i-1)
            j = min(bB2.bisect(base + 1), r)
            v += bA.sum(j-1) - bA.sum(i-1)
            v = max(v + A[j-1], v * B[j-1])
            i = j+1
        ans.append(v)

print(*ans, sep="\n")
