T = int(input())

def solve(A: list, B: list, N: int, M: int):
    A.sort()
    B.sort(reverse=True)
    # print(A, B)
    dp = [-1]
    for i in range(N):
        j = dp[-1] + 1
        if A[i] + B[j] >= M:
            dp.append(j)
        else:
            dp.append(dp[-1])
    n = 0
    for i in range(N):
        p, c = dp[i], dp[i+1]
        if c != -1 and p != c:
            n += 1
    minv = sum(a + b for a, b in zip(A, B)) - n * M
    return minv

ans = []
for _ in range(T):
    N, M = map(int, input().split())
    # mod = lambda x: int(x)%M
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans.append(solve(A, B, N, M))

print(*ans, sep="\n")
