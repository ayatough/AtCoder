N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort()

D = []
for i in range(N-1):
    D.append(X[i+1] - X[i])

D.sort(reverse=True)

print(sum(D[M-1:]))
