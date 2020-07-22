N = int(input())
L = list(map(int, input().split()))
LM = 2000
L.sort()
dp = [0] * LM
pp = [0] * LM
for l in range(L[0] + L[1]):
    dp[l] = 1

ans = 0
for i in range(2,N):
    pp = dp
    dp = [0] * LM
    for l in range(L[0]+L[i]):
        dp[l] = pp[l] + i
    j = 1
    for l in range(L[0]+L[i], L[i]+L[i-1]):
        if l >= L[i] + L[j]:
            j += 1
        dp[l] = pp[l] + i - j
    ans += pp[L[i]]

print(ans)
