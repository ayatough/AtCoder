from random import randint

N, K = map(int, input().split())
AMax = 9

X = []
for _ in range(N):
    X.append(randint(1, N))

A = []
for _ in range(N):
    A.append(randint(1, AMax))


print(N, K)
print(*X)
print(*A)

