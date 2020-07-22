N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
T = [2, 5, 5, 4, 5, 6, 3, 7, 6]

H = set(T[a-1] for a in A)
H = list(H)
H.sort()

dp = [-1 for _ in range(N+1)]
dp[0] = 0

for i in range(1,N+1):
    ret = 0
    if i-H[0] < 0:
        continue
    dp[i] = max(dp[i-h] + 1 for h in H if i-h>=0)

ans = ''
j = N
for i in range(1,dp[-1]):
    for a in A:
        if dp[j-T[a-1]] == dp[j] - 1:
            ans += str(a)
            j -= T[a-1]
            break

for a in A:
    if j == T[a-1]:
        ans += str(a)
        j -= T[a-1]
        break

print(ans)
