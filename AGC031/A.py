from collections import Counter
N = int(input())
S = input()
MOD = 10**9 + 7

C = Counter(S)
ans = 1
for v in C.values():
    ans *= (v+1)
    ans %= MOD

print((ans-1) % MOD)
