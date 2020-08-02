from math import ceil
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

def possible(x):
    count = 0
    for a in A:
        if a <= x:
            return True
        count += int(ceil(a/x)) - 1
        if count > K:
            return False
    return True

def solve():
    lo, hi = 0, A[0]
    while lo < hi-1:
        mi = (hi + lo) // 2
        if possible(mi):
            hi = mi
        else:
            lo = mi
    return hi

if __name__ == "__main__":
    print(solve())
