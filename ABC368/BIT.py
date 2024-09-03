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

if __name__ == "__main__":
    bit = BIT(8)
    bit.add(3, 4)
    bit.add(1, 9)
    bit.add(1, -2)
    bit.add(7, 1)

    print(bit.bit)

    for i in range(1, 8+1):
        print(bit.sum(i))

    bit.update(1, 0)
    bit.update(5, 10)

    for i in range(1, 8+1):
        print(bit.sum(i))


    for i in range(17):
        print("bisect: ", i, ", ", bit.bisect(i))
