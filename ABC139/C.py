N = int(input())
H = list(map(int, input().split()))

cur = 0
ans = 0
for i in range(1,N):
    if H[i] <= H[i-1]:
        cur += 1
    else:
        cur = 0
    if ans < cur:
        ans = cur

print(ans)
