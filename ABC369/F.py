from bisect import bisect_left, bisect_right

H, W, N = map(int, input().split())
INF = 10**15

RC = []
for _ in range(N):
    r, c = map(int, input().split())
    RC.append((r, c))

RC.sort()

# print(RC)

# LIS

dp = [INF for _ in range(N)]
pre = [-1 for _ in range(N)]
for i in range(N):
    _, c = RC[i]
    j = bisect_right(dp, c)
    dp[j] = c
    pre[i] = j + 1

# print(dp)
# print(pre)

npick = bisect_left(dp, INF)
print(npick)
seq = [(H, W)]

for i in range(N-1, -1, -1):
    if pre[i] == npick:
        seq.append(RC[i])
        npick -= 1

seq.append((1, 1))
# print(seq)

path = []
for i in range(len(seq) - 2, -1, -1):
    nd = seq[i][0] - seq[i+1][0]
    nr = seq[i][1] - seq[i+1][1]
    path += "D" * nd + "R" * nr

print(*path, sep="")
