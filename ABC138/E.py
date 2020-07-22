from bisect import bisect
S = input()
T = input()
LS = len(S)
LT = len(T)

H = {chr(i): [] for i in range(ord('a'), ord('z')+1)}
for i, s in enumerate(S):
    H[s].append(i)

dp = [0] * (LT+1)
dp[0] = -1
valid = True

for i in range(1,LT+1):
    t = T[i-1]
    p = dp[i-1] % LS if i > 1 else -1
    if len(H[t]) == 0:
        valid = False
        break
    q = bisect(H[t], p)
    if q == len(H[t]):
        dp[i] = dp[i-1] + LS - p + H[t][0]
    else:
        dp[i] = dp[i-1] + H[t][q] - p

print(dp[-1] + 1 if valid else -1)
