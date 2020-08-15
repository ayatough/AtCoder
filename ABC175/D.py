N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
INF = 10**9+1

def solve():
    ans = -INF

    for i in range(N):
        memo = [0] * (N+1)
        j = 0
        p = i
        while j < N:
            memo[j+1] = memo[j] + C[p]
            p = P[p] - 1
            j += 1
            if p == i:
                break
        tans =-INF
        if memo[j] > 0:
            for k in range(j):
                q = (K-k-1) // j
                tans = max(tans, memo[k+1] + memo[j] * q)
        else:
            for k in range(min(K, j)):
                tans = max(tans, memo[k+1])

        ans = max(ans, tans)
    return ans

if __name__ == "__main__":
    print(solve())
