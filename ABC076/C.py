S = input()
T = input()

def slv(S, T):
    cnd = []
    for i in range(len(S) - len(T) + 1):
        a = ''
        for j in range(len(T)):
            if S[i+j] in ('?', T[j]):
                a += T[j]
                continue
            break
        if len(a) == len(T):
            for j in range(i-1, -1, -1):
                a = ('a' if S[j] == '?' else S[j]) + a
            for j in range(i + len(T), len(S)):
                a += ('a' if S[j] == '?' else S[j])
            cnd.append(a)
    if len(cnd) == 0:
        return 'UNRESTORABLE'
    cnd.sort()
    return cnd[0]

print(slv(S, T))
