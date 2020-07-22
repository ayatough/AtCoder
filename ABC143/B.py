from itertools import combinations
N = int(input())
D = list(map(int, input().split()))
print(sum(d1*d2 for d1, d2 in combinations(D, 2)))
