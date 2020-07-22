from collections import Counter
N = int(input())
MAXBIT = 60
MOD = 10 ** 9 + 7
A = list(map(int, input().split()))
B = []
C = [[] for _ in range(MAXBIT)]
for a in A:
    for d in range(MAXBIT):
        C[d].append(a >> d & 1)
ans = 0
for d in range(MAXBIT):
    num0 = C[d].count(0)
    num1 = N - num0
    ans += ((num0 * num1) % MOD) * pow(2, d, MOD)
    ans %= MOD
print(ans)