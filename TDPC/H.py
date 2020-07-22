from collections import defaultdict
N, W, C = map(int, input().split())
B = defaultdict(list)

for _ in range(N):
    w, v, c = map(int, input().split())
    B[c].append((w, v))

S = len(B.keys())

dp, pp = [], []
for _ in range(C+1):
    d, p = [], []
    for _ in range(S+1):
        d.append([0] * (W+1))
        p.append([0] * (W+1))
    dp.append(d)
    pp.append(p)

color = 0
ans = 0
for b in B.values():
    color += 1
    for (weight, value) in b:
        pp, dp = dp, pp
        for c in range(1, C+1):
            for w in range(1, W+1):
                for lc in range(color+1):
                    dp[c][lc][w] = pp[c][lc][w]
                if w >= weight:
                    plus = dp[c][color][w]
                    for lc in range(color+1):
                        plus = max(pp[c-(lc!=color)][lc][w-weight] + value, plus)
                    dp[c][color][w] = plus
                    ans = max(ans, plus)

print(ans)
