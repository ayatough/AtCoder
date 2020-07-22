N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
res = 0
for i in range(N):
    enm = min(A[i]+A[i+1]-res, B[i])
    res = max(res + enm - A[i], 0)
    cnt += enm

print(cnt)
