N, K = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * (N+1)
for i, a in enumerate(A):
    B[i+1] = B[i] + a%K
for i in range(N+1):
    B[i] -= i
    B[i] %= K
ans = 0
# compress
C = B[::]
C.sort()
I = dict()
itmp = 0
I[C[0]] = 0
for i in range(1, N+1):
    if C[i] != C[i-1]:
        itmp += 1
        I[C[i]] = itmp

tbl = [0] * (N+1)
for i in range(min(K,N+1)):
    tbl[I[B[i]]] += 1
    ans += tbl[I[B[i]]] - 1
for i in range(K, N+1):
    tbl[I[B[i-K]]] -= 1
    tbl[I[B[i]]] += 1
    ans += tbl[I[B[i]]] - 1
print(ans)
