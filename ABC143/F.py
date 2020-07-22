from collections import Counter
N = int(input())
A = list(map(int, input().split()))
C = list(Counter(A).values())
D = [0] * (N+1)
for k, d in Counter(C).items():
    D[k] = d

ckd, cd = [0] * (N+1), [0] * (N+1)

for i in range(1,N+1):
    cd[i] = cd[i-1] + D[i]
    ckd[i] = ckd[i-1] + i*D[i]

INF = float('inf')
def f(x):
    if x:
        return (x*(cd[-1] - cd[x]) + ckd[x]) // x
    return INF

cur = N
v = f(cur)
for k in range(1,N+1):
    while k > v:
        cur -= 1
        v = f(cur)
    print(cur)
