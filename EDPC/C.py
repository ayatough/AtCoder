# input
N = int(input())
A = []
B = []
C = []
for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

dp = [{'a': None, 'b': None, 'c': None} for _ in range(N+1)]
dp[0]['a'] = 0
dp[0]['b'] = 0
dp[0]['c'] = 0

for i in range(1, N+1):
    dp[i]['a'] = max(dp[i-1]['b'] + A[i-1], dp[i-1]['c'] + A[i-1])
    dp[i]['b'] = max(dp[i-1]['c'] + B[i-1], dp[i-1]['a'] + B[i-1])
    dp[i]['c'] = max(dp[i-1]['a'] + C[i-1], dp[i-1]['b'] + C[i-1])

print(max(dp[-1].values()))
