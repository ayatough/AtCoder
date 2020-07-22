from collections import Counter
from itertools import product
N = int(input())
V = list(map(int, input().split()))

c0mc = Counter(V[::2]).most_common(2)
c1mc = Counter(V[1::2]).most_common(2)
# [0] is error avoidance
if len(c0mc) == 1:
    c0mc.append((0, 0))
if len(c1mc) == 1:
    c1mc.append((0, 0))

print(N - max(a[1] + b[1] for (a, b) in product(c0mc, c1mc) if a[0] != b[0]))
