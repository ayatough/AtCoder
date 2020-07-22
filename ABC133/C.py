from itertools import combinations
L, R = map(int, input().split())
A = 2019
M = min(R+1, L+A)

a = min(i % A for i in range(L, M))
if a == 0:
    print(0)
else:
    print(min((i*j) % A for (i, j) in combinations(range(L, R+1), 2)))
    # print(min((a * (a+1)) % A, (b * (b+1)) % A))
