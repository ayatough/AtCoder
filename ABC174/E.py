from math import ceil
N, K = map(int, input().split())
A = list(map(int, input().split()))

def solve():
    memo = [[0, 0] for _ in range(N+1)]
    cum = 0
    tot = sum(A)
    A.sort(reverse=True)
    for i in range(1,N+1):
        a = A[i-1]
        pre = cum
        cum += a
        plo = pre * K // tot
        phi = int(ceil(pre * K / tot))
        clo = cum * K // tot
        chi = int(ceil(cum * K / tot))
        memo[i][0] = min(max(memo[i-1][0], a / max(1,clo-plo+1)), max(memo[i-1][1], a / max(1,clo-phi+1)))
        memo[i][1] = min(max(memo[i-1][0], a / max(1,chi-plo+1)), max(memo[i-1][1], a / max(1,chi-phi+1)))
    return int(ceil(min(memo[-1])))

if __name__ == "__main__":
    print(solve())
