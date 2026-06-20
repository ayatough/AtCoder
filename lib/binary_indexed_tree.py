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

    def set(self, l, r, a):
        """ [l, r)
        """
        self._set(0, l, a)
        self._set(0, r, -a)
        self._set(1, l, -(l-1)*a)
        self._set(1, r, (r-1)*a)

    def _set(self, p, i, a):
        v = self._sum(p, i) - self._sum(p, i - 1)
        self._add(p, i, a - v)

    def sum(self, i):
        return self._sum(0, i) * i + self._sum(1, i)

    def _sum(self, p, i):
        s = 0
        while i > 0:
            s += self.bit[p][i]
            i -= i & -i
        return s


if __name__ == "__main__":
    bit = BIT(100)
    bit.add(3, 34)
    print(bit.sum(2), bit.sum(3), bit.sum(4))

    bit_raq = BIT_RAQ(100)
    bit_raq.add(4, 8, 1)
    bit_raq.add(7, 10, 1)
    for i in range(1, 13):
        print(i, bit_raq.sum(i) - bit_raq.sum(i-1))

    bit_raq.set(2, 6, 3)
    for i in range(1, 13):
        print(i, bit_raq.sum(i) - bit_raq.sum(i-1))
