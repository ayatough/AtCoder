import sys
N, M = map(int, input().split())
MOD = 10 ** 9 + 7
NMAX = 10 ** 5
sys.setrecursionlimit(10 ** 6)

memo = [None for _ in range(NMAX+1)]
def fibo(n):
    if memo[n]:
        return memo[n]
    if n == 0:
        return 0
    elif n < 3:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

nc = 1
b = 0
for i in range(M):
    a = int(input())
    nc = (nc * fibo(a - b)) % MOD
    b = a + 1

nc = (nc * fibo(N + 1 - b)) % MOD

print(nc)
