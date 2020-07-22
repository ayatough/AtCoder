from itertools import combinations
N, D = map(int, input().split())
X = []
for _ in range(N):
    X.append(list(map(int, input().split())))

def dist2(x, y):
    return sum((a-b)**2 for (a, b) in zip(x, y))

def judge(d):
    m = int(d ** 0.5)
    return m*m == d

cnt = 0
for p in combinations(X, 2):
    x, y = p
    cnt += 1 if judge(dist2(x, y)) else 0

print(cnt)
