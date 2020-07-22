from itertools import permutations
N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
ans = 0
cnt = 0
for p in permutations(range(N)):
    path = 0
    for i in range(1,N):
        path += ((X[p[i]]-X[p[i-1]])**2+(Y[p[i]]-Y[p[i-1]])**2)**0.5
    ans += path
    cnt += 1
print(ans / cnt)