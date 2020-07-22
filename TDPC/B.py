A, B = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
X.reverse()
Y.reverse()

dn = [[0 for _ in range(B+1)] for _ in range(A+1)]
dm = [[0 for _ in range(B+1)] for _ in range(A+1)]

dn[1][0] = X[0]
dn[0][1] = Y[0]

for i in range(2,A+1):
    dn[i][0] = dn[i-2][0] + X[i-1]
    dm[i][0] = dn[i-1][0]

for j in range(2,B+1):
    dn[0][j] = dn[0][j-2] + Y[j-1]
    dm[0][j] = dn[0][j-1]

for i in range(1,A+1):
    for j in range(1,B+1):
        a, b = dm[i-1][j] + X[i-1], dm[i][j-1] + Y[j-1]
        if a > b:
            dn[i][j] = a
            dm[i][j] = dn[i-1][j]
        else:
            dn[i][j] = b
            dm[i][j] = dn[i][j-1]

print(dn[-1][-1])
