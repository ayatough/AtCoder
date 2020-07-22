N = int(input())
A = list(int(input()) for _ in range(N))
asc, des = [0], [0]
for i in range(N-1):
    asc.append(max(asc[-1], A[i]))
    des.append(max(des[-1], A[-1-i]))

for i in range(N):
    print(max(asc[i], des[-1-i]))
