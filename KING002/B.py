from collections import Counter
N = int(input())
D = list(map(int, input().split()))
MOD = 998244353
C = Counter(D)
ans = 0
if C[0] != 1 or D[0] != 0:
    print(ans)
else:
    for i, n in C.items():
        if i == 0:
            ans = 1
            continue
        ans *= pow(C[i-1], n, MOD)
        ans %= MOD
    print(ans)
