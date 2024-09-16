N, M = map(int, input().split())
A = list(map(int, input().split()))

MOD = [0] * M
m = A[0]
MOD[m % M] += 1

for a in A[1:-1]:
    m = (m + a) % M
    MOD[m % M] += 1
m = (m + A[-1]) % M

a = 0
ans = MOD[0]

for i in range(N-1):
    j = a
    a = (- A[i] + a + M) % M
    if MOD[(A[i] - j + M) % M] > 0:
        MOD[(A[i] - j + M) % M] -= 1
        MOD[(m - A[i] - a + M) % M] += 1
    ans += MOD[(M - a) % M]

print(ans)
