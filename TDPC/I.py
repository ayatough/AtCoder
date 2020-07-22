from functools import lru_cache
import sys
sys.setrecursionlimit(300**2)

S = input()

@lru_cache(maxsize=None)
def dfs(l, r):
    if r - l < 3:
        return 0
    if r - l == 3:
        return 3 if S[l:r] == 'iwi' else 0
    cnd = max(dfs(l, m) + dfs(m, r) for m in range(l+1, r))
    if S[l] == S[r-1] == 'i' and (r - l) % 3 == 0:
        for m in range(l+1, r-1, 3):
            if S[m] == 'w' and dfs(l+1, m) == m-l-1 and dfs(m+1, r-1) == r-m-2:
                cnd = max(cnd, r-l)
    return cnd

print(dfs(0, len(S)) // 3)
