from collections import Counter
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cb = Counter(B)
ca = Counter()

n = N  # max
for a in A:
    ca.update([a])
    n = min(n, cb[a] // ca[a])
    print(n)
