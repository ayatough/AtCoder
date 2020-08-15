R, C, K = map(int, input().split())
RC = [[0] * C] for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    RC[r-1][c-1] = v


def solve():
    memo = [[[0] * 4 for _ in range(C+1)] for _ in range(R+1)]
    for r in range(1,R+1):
        for c in range(1,C+1):
            v = RC[r][c]
            # case 0
            memo[r][c][0] = max(memo[r-1][c][3], memo[r][c-1][0])
            memo[r][c][1] = max(memo[r][c][0] + v, )
            if RC[r][c] > 0:
                # from up
                memo[r][c][0] = memo[r-1][c][3] + RC[r][c]
                # from left
                for i in range(3):
                    if memo[r][c][i+1] > memo[r][c][i] + RC[r][c]:
                        memo[r][c][i+1] = 
            for i in range(3):
                memo[r][c][i+1] = max(memo[r][c][i], memo[r][c][i+1])




if __name__ == "__main__":
    print(solve())
