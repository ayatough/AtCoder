N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
INF = 10**9+1

def solve():
    cycles = []
    memo = [False] * N
    i = 0
    while i < N-1:
        cycle = []
        j = i
        while not memo[j]:
            cycle.append(j)
            memo[j] = True
            j = P[j] - 1
        k = i
        for i in range(k, N):
            if not memo[i]:
                break
        cycles.append(cycle)

    ans = -INF

    for cycle in cycles:
        n = len(cycle)
        # q, r = divmod(K-1, n)
        # r += 1
        memo = [-INF] * n
        for i in range(n):
            s = 0
            for j in range(n):
                s += C[cycle[(i+j)%n]]
                memo[j] = max(memo[j], s)
        tmpmax = -INF
        imax = -1
        if K < n:
            for i in range(K):
                if tmpmax < memo[i]:
                    tmpmax = memo[i]
                    imax = i+1
        else:
            if memo[-1] > 0:
                for i in range(n):
                    q = (K-i-1) // n
                    tmpmax = max(tmpmax, memo[i] + memo[-1] * q)
            else:
                for i in range(n):
                    tmpmax = max(tmpmax, memo[i])

        ans = max(ans, tmpmax)
    return ans

if __name__ == "__main__":
    print(solve())
