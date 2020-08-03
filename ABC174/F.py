import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
C = list(map(int, input().split()))
LRST = []
for i in range(Q):
    l, r = map(int, input().split())
    LRST.append((l-1, 0, r-1, i))


class FenwickTree(object):
    def __init__(self, n):
        self._bit = [0] * (n+1)
        self.n = n+1
    
    def add(self, i, a):
        i += 1
        while i < self.n:
            self._bit[i] += a
            i += i & -i
    
    def sum(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self._bit[i]
            i -= i & -i
        return ret


def solve():
    memo = [-1] * N
    for i, c in enumerate(C):
        if memo[c-1] >= 0:
            LRST.append((memo[c-1], 1, i, -1))
        memo[c-1] = i
    LRST.sort(reverse=True)
    ans =[0 for _ in range(Q)]
    ft = FenwickTree(N+1)
    for sl, typ, tr, q in LRST:
        if typ == 1:
            ft.add(tr, 1)
        else:
            ans[q] = tr - sl + 1 - ft.sum(tr)
    for a in ans:
        print(a)


if __name__ == "__main__":
    solve()
