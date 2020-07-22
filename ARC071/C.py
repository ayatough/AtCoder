from collections import Counter
N = int(input())
cum = Counter(input())
for _ in range(N-1):
    cum &= Counter(input())

print(''.join(sorted(cum.elements())))
