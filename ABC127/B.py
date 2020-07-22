R, D, X = map(int, input().split())

for i in range(2001, 2011):
    X = R * X - D
    print(X)
