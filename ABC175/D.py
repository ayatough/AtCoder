N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
INF = 10**9+1

def solve():
    q, r = divmod(K, N)
    if r == 0:
        q -= 1
        r = N
    
    m = -INF

    

    # memo = [[-INF] * N for _ in range(N-1)]
    # memomax = [-INF] * (N-1)
    # memo[0] = C.copy()
    # memomax[0] = max(memo[0])
    # for i in range(1,N-1):
    #     tmp = -INF
    #     for j in range(N):
    #         memo[i][j] = memo[i-1] + P[i]

    # s = C[0]
    # i = P[0]-1
    # j = 0
    # for _ in range(r-1):
    #     s += C[i]
    #     i = P[i]-1
    # m = max(m, s)

    # for _ in range(r-1):
    #     tmp = m - C[j] + C[i]
    #     m = max(m, tmp)
    #     j = P[j]-1
    #     i = P[i]-1

    if q == 0


if __name__ == "__main__":
    print(solve())
