N = int(input())

A = [[[0] * (N+1) for _ in range(N+1)] for _ in range(N+1)]

for i in range(N**2):
    i, j = divmod(i, N)
    A[i+1][j+1][1:] = list(map(int, input().split()))

for i in range(N):
    for j in range(N):
        for k in range(N):
            A[i+1][j+1][k+1] += A[i+1][j+1][k]

for i in range(N):
    for k in range(N):
        for j in range(N):
            A[i+1][j+1][k+1] += A[i+1][j][k+1]

for j in range(N):
    for k in range(N):
        for i in range(N):
            A[i+1][j+1][k+1] += A[i][j+1][k+1]

Q = int(input())

for i in range(Q):
    li, ri, lj, rj, lk, rk = map(int, input().split())
    li -= 1
    lj -= 1
    lk -= 1
    l = A[li][rj][rk] - A[li][lj][rk] - A[li][rj][lk] + A[li][lj][lk]
    r = A[ri][rj][rk] - A[ri][lj][rk] - A[ri][rj][lk] + A[ri][lj][lk]
    print(r - l)
