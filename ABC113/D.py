from itertools import product
H, W, K = map(int, input().split())
MOD = 10 ** 9 + 7

dp = [0] * W
pp = [0] * W

dp[0] = 1

for h in range(1,H+1):
    dp, pp = pp, dp
    dp = [0] * W
    # 一行における横棒のパターンを全探索
    for bs in product((0,1), repeat=W-1):
        swaps = []
        throughs = []
        # validity check and swap or through
        valid = True
        for i in range(1,W-1):
            if bs[i] == bs[i-1] == 1:
                valid = False
                break
        if not valid:
            continue
        for i in range(W-1):
            if bs[i]:
                swaps.append((i,i+1))
            else:
                if len(swaps) == 0 or swaps[-1][-1] != i:
                    throughs.append(i)
        if len(swaps) == 0 or swaps[-1][-1] != W-1:
            throughs.append(W-1)
        for s in swaps:
            dp[s[0]] += pp[s[1]]
            dp[s[1]] += pp[s[0]]
            dp[s[0]] %= MOD
            dp[s[1]] %= MOD
        for t in throughs:
            dp[t] += pp[t]
            dp[t] %= MOD

print(dp[K-1])
