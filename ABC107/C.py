N, K = map(int, input().split())
X = list(map(int, input().split()))
INF = float('inf')
ans = INF
l, r = 0, K-1
for i in range(N-K+1):
    a, b = X[l+i], X[r+i]
    A, B = abs(a), abs(b)
    if a*b > 0:
        ans = min(ans, max(A, B))
    else:
        ans = min(ans, A + B + (A if A < B else B))

print(ans)
