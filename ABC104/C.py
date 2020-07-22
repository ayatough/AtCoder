from itertools import product
D, G = map(int, input().split())
P, C = [], []
for _ in range(D):
    p, c = map(int, input().split())
    P.append(p)
    C.append(c)

def make_pat(i):
    pat = [[0, 1]] * i + [[0]] + [[0, 1]] * (D-i-1)
    return product(*pat)

min_ = sum(p for p in P)
for i in range(D):
    for pat in make_pat(i):
        scr = sum(P[j] * (j+1) * 100 + C[j] for (j, p) in enumerate(pat) if p == 1)
        num = sum(P[j] for (j, p) in enumerate(pat) if p == 1)
        for k in range(P[i]):
            zbn = k * (i+1) * 100 + (0 if k < P[i] else C[i])
            if scr + zbn >= G:
                if min_ > num + k:
                    min_ = num + k
                break

print(min_)
