from collections import Counter
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [0]
for a in A:
    B.append((B[-1]+a) % M)
B = Counter(B)
ans = 0
for c in B.values():
    ans +=  c*(c-1)//2
print(ans)
