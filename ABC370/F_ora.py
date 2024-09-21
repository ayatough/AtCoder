from itertools import combinations

N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [0]

for a in A:
    B.append(B[-1] + a)

INF = 2*10*9
best_min_w = INF

best = [0, set()]

for cuts in combinations(range(N), K):
    W = [B[-1] - B[cuts[-1]] + B[cuts[0]]]
    minw = W[-1]
    for i in range(1,K):
        W.append(B[cuts[i]] - B[cuts[i-1]] )
        minw = min(minw, W[-1])

    if minw > best[0]:
        best[0] = minw
        best[1] = set({*cuts})
    elif minw == best[0]:
        best[1] |= set({*cuts})

print(best[0], N - len(best[1]))
