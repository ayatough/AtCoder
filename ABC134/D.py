N = int(input())
A = list(map(int, input().split()))

B = [0 for _ in range(N)]

for i, a in enumerate(A[::-1]):
    i = N - i
    v = B[i-1]
    for j in range(i*2, N+1, i):
        v ^= B[j-1]
    if v != a:
        B[i-1] ^= 1

M = len([b for b in B if b == 1])
print(M)
for i, b in enumerate(B):
    if b == 1:
        print(i+1)
