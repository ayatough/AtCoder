N, K = map(int, input().split())
H = []
for _ in range(N):
    H.append(int(input()))
INF = float('inf')

H.sort()
ans = INF
for i in range(K-1, N):
    ans = min(ans, H[i] - H[i-K+1])

print(ans)
