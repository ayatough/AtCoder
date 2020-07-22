from functools import lru_cache
N = int(input())
A = list(map(int, input().split()))

@lru_cache(maxsize=None)
def dfs(l, r, wl, wr):
    if r <= l + 1:
        return 0
    v = min(dfs(l, m, wl, wl+wr) + dfs(m, r, wl+wr, wr) + A[m] * (wl+wr) for m in range(l+1, r))
    return v

print(dfs(0, N-1, 1, 1) + A[0] + A[N-1])
