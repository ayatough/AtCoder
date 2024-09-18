

H, W, Q = map(int, input().split())

# RC = []
# for _ in range(Q):
#     RC.append(tuple(map(int, input().split())))

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

# ROW = [BIT(W) for _ in range(H+1)]
# COL = [BIT(H) for _ in range(W+1)]

ROW = []
for i in range(H+1):
    bit = BIT(W)
    for j in range(1,W+1):
        bit.add(j, 1)
    ROW.append(bit)

COL = []
for i in range(W+1):
    bit = BIT(H)
    for j in range(1,H+1):
        bit.add(j, 1)
    COL.append(bit)

def view():
    print(R, C)
    for b in ROW[1:]:
        s = ""
        for i in range(1,W+1):
            s += "#" if b.sum(i) - b.sum(i-1) == 1 else " "
        print(s)

for _ in range(Q):
    R, C = map(int, input().split())
    if ROW[R].sum(C) - ROW[R].sum(C-1) == 1:
        ROW[R].add(C, -1)
        COL[C].add(R, -1)
    else:
        left = ROW[R].bisect(ROW[R].sum(C))
        right = ROW[R].bisect(ROW[R].sum(C)+1)
        top = COL[C].bisect(COL[C].sum(R))
        bottom = COL[C].bisect(COL[C].sum(R)+1)

        if left > 0:
            ROW[R].add(left, -1)
            COL[left].add(R, -1)
        if right <= W:
            ROW[R].add(right, -1)
            COL[right].add(R, -1)
        if top > 0:
            ROW[top].add(C, -1)
            COL[C].add(top, -1)
        if bottom <= H:
            ROW[bottom].add(C, -1)
            COL[C].add(bottom, -1)
    # view()

print(sum(bit.sum(W) for bit in ROW[1:]))
