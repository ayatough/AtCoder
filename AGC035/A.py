from collections import Counter
N = int(input())
A = list(map(int ,input().split()))
C = Counter(A)
MAXD = 30
B = [('0' * MAXD + bin(a)[2:])[-30:] for a in A]

ps = []
res = True
for i in range(MAXD):
    bs = list(b[i] for b in B)
    c = Counter(bs)
    if c['0'] == N:
        continue
    if c['0'] == N // 3:
        if N % 3 == 0:
            if len(ps) != 0:
                if all(p == b for (b, p) in zip(bs, ps)):
                    continue
                bc = Counter(int(p + b, 2) for (b, p) in zip(bs, ps))
                if c[0] == 0 and c[1] == c[2] == c[3]:
                    continue
            ps = bs.copy()
            continue
    res = False
    break

print('Yes' if res else 'No')
