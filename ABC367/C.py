from itertools import product

N, K = map(int, input().split())
R = list(map(int, input().split()))

for rs in product(*[range(1, r+1) for r in R]):
    if sum(rs) % K == 0:
        print(*rs)
