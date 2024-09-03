N = int(input())

L = []
R = []

for _ in range(N):
    a, s = input().strip().split()
    if s == 'R':
        R.append(int(a))
    else:
        L.append(int(a))

F = 0

for i in range(len(L) - 1):
    F += abs(L[i+1] - L[i])

for i in range(len(R) - 1):
    F += abs(R[i+1] - R[i])

print(F)
