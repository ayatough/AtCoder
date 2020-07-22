# input
A, B, Q = map(int, input().split())
S, T, X = [], [], []
for _ in range(A):
    S.append(int(input()))

for _ in range(B):
    T.append(int(input()))

for _ in range(Q):
    X.append(int(input()))

# end of world
EOW = 10 ** 10

# boundary info
tbounds = [(T[i+1] + T[i]) // 2 for i in range(B-1)]
sbounds = [(S[i+1] + S[i]) // 2 for i in range(A-1)]

# add pivot
tbounds.insert(0, 0)
tbounds.append(EOW)
sbounds.insert(0, 0)
sbounds.append(EOW)

# temple to shrine
ttos = []
cur = 0
for i in range(B):
    while True:
        if T[i] <= sbounds[cur]:
            break
        cur += 1
    ttos.append(cur-1)

# shrine to temple
stot = []
cur = 0
for i in range(A):
    while True:
        if S[i] <= tbounds[cur]:
            break
        cur += 1
    stot.append(cur-1)

for x in X:
    snear = 0
    while True:
        if x <= sbounds[snear]:
            break
        snear += 1
    tnears_range = range(max(0, stot[snear-1]), min(stot[snear-1] + 4, B))
    best = abs(S[snear-1]-x) + abs(T[stot[snear-1]]-S[snear-1])
    for j in tnears_range:
        dist = abs(T[j]-x) + abs(S[ttos[j]]-T[j])
        if dist < best:
            best = dist
    # svisit = 0
    # tnear = 0
    # best = EOW * 2
    # # search
    # for i in range(A):
    #     tnear = stot[i]
    #     dist = abs(S[i]-x) + abs(T[tnear]-S[i])
    #     if best > dist:
    #         best = dist
    #     else:
    #         break
    # for i in range(max(0, tnear-3), min(tnear+3, B)):
    #     snear = ttos[i]
    #     dist = abs(T[i]-x) + abs(S[snear]-T[i])
    #     if best > dist:
    #         best = dist
    print(best)
    # print(min(min(abs(S[i]-x) + abs(T[nt]-S[i]) for (i, nt) in enumerate(stot)), min(abs(T[i]-x) + abs(S[ns]-T[i]) for (i, ns) in enumerate(ttos))))
