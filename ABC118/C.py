N = int(input())
A = list(map(int, input().split()))

ans = A[0]
for i in range(1,N):
    bns = A[i]
    l = max(ans, bns)
    s = min(ans, bns)
    while l % s != 0:
        l, s = s, l % s
    ans = s

print(ans)
