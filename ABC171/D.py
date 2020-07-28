import sys
import numpy as np

input = sys.stdin.readline

def minus(a):
    return int(a)-1

M = 10**5
N = int(input())
A = list(map(minus, input().split()))
Q = int(input())


def solve():
    hist = list(np.histogram(A, M, (0, M))[0].astype(int))
    cur = sum(A) + N
    for _ in range(Q):
        b, c = map(minus, input().split())
        dh = hist[b]
        cur += dh*(c-b)
        hist[b] -= dh
        hist[c] += dh
        print(cur)

if __name__ == "__main__":
    solve()
