S = input()
T = input()

# dp = [[[] for _ in range(len(S)+1)] for _ in range(len(T)+1)]
cdp = [[None for _ in range(len(S)+1)] for _ in range(len(T)+1)]
ddp = [[None for _ in range(len(S)+1)] for _ in range(len(T)+1)]
# dp[0] = [[''] for _ in range(len(S)+1)]
cdp[0] = [0 for _ in range(len(S)+1)]
ddp[0] = [0 for _ in range(len(S)+1)]

for i in range(1,len(T)+1):
    for j in range(len(S)+1):
        if j == 0:
            # dp[i][j] = ['']
            cdp[i][j] = 0
            ddp[i][j] = 0
            continue
        if S[j-1] == T[i-1]:
            # dp[i][j] = [p + S[j-1] for p in dp[i-1][j-1]]
            cdp[i][j] = cdp[i-1][j-1] + 1
            ddp[i][j] = 2
        else:
            if cdp[i][j-1] > cdp[i-1][j]:
                # dp[i][j] = dp[i][j-1]
                cdp[i][j] = cdp[i][j-1]
                ddp[i][j] = 1
            else:
                # dp[i][j] = dp[i-1][j]
                cdp[i][j] = cdp[i-1][j]
                ddp[i][j] = 0

# print(dp[-1][-1][0])

i, j = len(T), len(S)
L = ''
while i > 0 and j > 0:
    if ddp[i][j] == 2:
        i -= 1
        j -= 1
        L += T[i]
    elif ddp[i][j] == 1:
        j -= 1
    elif ddp[i][j] == 0:
        i -= 1

print(L[::-1])
