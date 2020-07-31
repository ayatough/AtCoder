M = 201
X, N = map(int, input().split())
A = list(map(int, input().split()))


def solve():
    memo = [0] * M
    for a in A:
        d = a - X
        if d >= 0:
            memo[d*2] = 1
        else:
            memo[-d*2-1] = 1
    for i, m in enumerate(memo):
        if m == 0:
            if i % 2 == 0:
                return i//2 + X
            else:
                return -(i+1)//2 + X

if __name__ == "__main__":
    print(solve())
