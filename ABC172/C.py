from bisect import bisect

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def make_cum(ary):
    cum = [0]
    for v in ary:
        cum.append(cum[-1] + v)
    return cum


def solve():
    ans = 0
    cuma = make_cum(A)
    cumb = make_cum(B)
    for ia in range(N+1):
        if cuma[ia] > K:
            break
        ib = bisect(cumb, K-cuma[ia]) - 1
        ans = max(ans, ia + ib)
    return ans
        

if __name__ == "__main__":
    print(solve())
