# input
N = int(input())
H = list(map(int, input().split()))

dp = [None for _ in range(N)]
def jump(i):
    # initiate
    dp[0] = 0
    dp[1] = abs(H[1] - H[0])
    for i in range(2, N):
        dp[i] = min(dp[i-1] + abs(H[i]-H[i-1]), dp[i-2] + abs(H[i]-H[i-2]))
    # if i < 3 or H[i-2] < H[i-3]:
    #     cost += abs(H[i-2] - H[i-1]) + jump(i-1)
    # else:
    #     cost += abs(H[i-3] - H[i-1]) + jump(i-2)
    # dp[i] = cost
    # return cost
    return dp[N-1]

print(jump(N))
pass