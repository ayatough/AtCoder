import numpy as np
N, W, C = map(int, input().split())
B = np.zeros((N, 3), dtype=int)

for i in range(N):
    w, v, c = map(int, input().split())
    B[i] = [c, w, v]

B = B[np.argsort(B[:, 0])]
S = B[-1, 0]

dp = np.zeros((W+1, C+1, S+1), dtype=int)
pp = np.zeros((W+1, C+1, S+1), dtype=int)

for i in range(1, N+1):
    pp, dp = dp, pp
    color, weight, value = B[i-1]
    for w in range(1, W+1):
        for c in range(1, C+1):
            dp[w, c, :color+1] = pp[w, c, :color+1]
            if w >= weight:
                plus = np.max(pp[w-weight, c-1, :color] + value)
                plus = max(plus, pp[w-weight, c, color] + value)
                # plus = max(pp[w-weight, c-(lc!=color), lc] + value for lc in range(color+1))
                dp[w, c, color] = max(dp[w, c, color], plus)

print(np.max(np.max(dp[-1])))
