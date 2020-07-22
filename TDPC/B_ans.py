from sys import stdin
 
 
def dp_solve(a, b, ai, bi):
    dp = [[0]*(b+1) for _ in range(a+1)]
 
    # dp[i][j] = 残りの山の数が(i, j)の時に，すぬけ君がこれ以降にとる価値
    for i in range(a+1):
 
        for j in range(b+1):
            is_my_turn = ((a+b)-(i+j)) % 2 == 0
            if i == j == 0:
                pass
            elif i == 0:
                if is_my_turn:
                    dp[i][j] = dp[i][j-1]+bi[b-j]
                else:
                    dp[i][j] = dp[i][j-1]
            elif j == 0:
                if is_my_turn:
                    dp[i][j] = dp[i-1][j]+ai[a-i]
                else:
                    dp[i][j] = dp[i-1][j]
            else:
                if is_my_turn:
                    dp[i][j] = max(dp[i-1][j]+ai[a-i], dp[i][j-1] + bi[b-j])
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]
 
 
if __name__ == "__main__":
    a, b = map(int, input().split())
    ai = list(map(int, stdin.readline().split()))
    bi = list(map(int, stdin.readline().split()))
    print(dp_solve(a, b, ai, bi))
    pass