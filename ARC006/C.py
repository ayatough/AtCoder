N = int(input())
W = list(int(input()) for _ in range(N))
INF = 10 ** 5

T = []
for i in range(N):
    if len(T) == 0:
        T.append(W[i])
    else:
        k, dif = INF, INF
        for j, t in enumerate(T):
            if W[i] <= t:
                if dif > t - W[i]:
                    dif = t - W[i]
                    k = j
        if dif == INF:
            T.append(W[i])
        else:
            T[k] = W[i]

print(len(T))
