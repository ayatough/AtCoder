N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort()
A = list(y-x for x, y in zip(X, X[1:]))
A.sort(reverse=True)

print(sum(iter(A[N-1:])))
