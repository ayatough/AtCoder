class SEG:
    def __init__(self, n):
        self.n = 1 << len(bin(n-1)[2:])
        self.data = [0] * (self.n * 2 - 1)

    def update(self, i, x):
        i += self.n - 1
        self.data[i] = x
        while i > 0:
            i >>= 1
            self.data[i] = self.data[i<<1] + self.data[(i<<1)+1]

    def query(self, l, r):
        """ [l, r)
        """
        l += self.n - 1
        r += self.n - 1
        ret = 0
        while l < r:
            if r & 1:
                r -= 1
                ret += self.data[r]
            if l & 1:
                ret += self.data[l]
                l += 1
            l >>= 1
            r >>= 1
        return ret


class SEG_RUQ:
    def __init__(self, n):
        self.n = 1 << len(bin(n-1)[2:])
        self.data = [0] * (self.n * 2 - 1)
        self.lazy = [None] * (self.n * 2 - 1)

    def update(self, i, x):
        i += self.n - 1
        self.data[i] = x
        while i > 0:
            i >>= 1
            self.data[i] = self.data[i<<1] + self.data[(i<<1)+1]

    def query(self, l, r):
        """ [l, r)
        """
        l += self.n - 1
        r += self.n - 1
        ret = 0
        while l < r:
            self.eval()
            if r & 1:
                r -= 1
                ret += self.data[r]
            if l & 1:
                ret += self.data[l]
                l += 1
            l >>= 1
            r >>= 1
        return ret

    def eval(self, i):
        if self.lazy[i] is None:
            return
        if i < self.n - 1:
            self.lazy[(i<<1) + 0] = self.lazy[i] >> 1
            self.lazy[(i<<1) + 1] = self.lazy[i] >> 1
        self.data[i] = self.lazy[i]
        self.lazy[i] = None


if __name__ == "__main__":
    seg = SEG(100)
    seg.update(3, 8)
    seg.update(5, 1)
    for i in range(1, 11):
        print(i, i+3, seg.query(i,i+3))
