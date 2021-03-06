R, C, K = map(int, input().split())
RC = [[0] * C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    RC[r-1][c-1] = v


def solve():
    memo = [[0] * 4 for _ in range(C+1)]
    prev = [[0] * 4 for _ in range(C+1)]
    for r in range(1,R+1):
        prev, memo = memo, prev
        for c in range(1,C+1):
            v = RC[r-1][c-1]
            memo[c][0] = max(prev[c][3], memo[c-1][0])
            memo[c][1] = max(memo[c][0] + v, memo[c-1][1])
            memo[c][2] = max(memo[c][1], memo[c-1][1] + v, memo[c-1][2])
            memo[c][3] = max(memo[c][2], memo[c-1][2] + v, memo[c-1][3])
    return memo[-1][3]

if __name__ == "__main__":
    print(solve())
