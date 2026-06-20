T = int(input())

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

# for _ in range(T):
#     N = int(input())
#     A = list(map(int, input().split()))

#     # Brute
#     invalid = True
#     count = 0
#     while invalid:
#         # print(A)
#         for i in range(N-1):
#             a, b = A[i], A[i+1]
#             if a < b:
#                 continue
#             count += 1
#             A[i] -= 1
#             A[i+1] += 1
#             break
#         else:
#             invalid = False
#     print(count)

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    AA = A.copy()

    # Brute
    invalid = True
    count = 0
    while invalid:
        # print(A)
        for i in range(N-1):
            a, b = AA[i], AA[i+1]
            if a < b:
                continue
            count += 1
            AA[i] -= 1
            AA[i+1] += 1
            break
        else:
            invalid = False
    print("ans=", count)


    for i in range(N):
        A[i] -= i
    sums = [0] * N
    aves = [0] * N
    aves[0] = sums[0] = A[0]
    upds = []

    for i in range(1, N):
        sums[i] = sums[i-1] + A[i]
        aves[i] = sums[i] / (i + 1)
        if aves[i] < aves[i-1]:
            upds.append(i)

    mod = upds[-1] + 1
    a, b = divmod(sums[upds[-1]], mod)
    b = mod if b == 0 else b

    co = 0
    count = 0
    sign = 1
    for i in range(upds[-1], -1, -1):
        c = a if i < b else a + 1
        residual = co + c - A[i]
        print("(i, c, r, o) : ", i, c, residual, co)
        count += abs(residual)
        co = residual


    print(A)
    print(sums)
    print(aves)
    print(mod)
    print(a, b)
    print(count)
    print("="*20)
