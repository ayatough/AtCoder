N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9+7

def solve():
    A.sort(key=lambda x: abs(x), reverse=True)

    ans = 1
    nneg = 0
    a, b, c, d = -1, -1, -1, -1
    for k in range(K):
        ans = (ans * A[k])%MOD
        if A[k] < 0:
            nneg += 1
            b = k
        else:
            a = k
    
    if K == N or nneg%2 == 0:
        return ans
    
    for k in range(N-1, K-1, -1):
        if A[k] < 0:
            d = k
        else:
            c = k

    # b must be >= 0
    if a == -1 and c == -1: # all minus
        ans = 1
        for k in range(K):
            ans = (ans * A[-1-k])%MOD
        return ans
    
    if a == -1 or d == -1:
        outn = A[b]
        inn = A[c]
    elif c == -1:
        outn = A[a]
        inn = A[d]
    else:
        if A[a]*A[c] > A[b]*A[d]:
            outn = A[b]
            inn = A[c]
        else:
            outn = A[a]
            inn = A[d]

    ans = (ans * pow(outn, MOD-2, MOD))%MOD
    ans = (ans * inn)%MOD
    return ans

if __name__ == "__main__":
    print(solve())
