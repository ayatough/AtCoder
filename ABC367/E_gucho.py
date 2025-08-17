N, K = map(int, input().split())
X = [-1]
X.extend(list(map(int, input().split())))
A = [-1]
A.extend(list(map(int, input().split())))

ans = [-1] * (N+1)

for i in range(1, N+1):
    j = i
    for _ in range(K):
        j = X[j]
    ans[i] = A[j]

print(*ans[1:])
