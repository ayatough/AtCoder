# input
N = int(input())
S = input()
T = input()

def dist(s, t):
    long, short = (s, t) if len(s) > len(t) else (t, s)
    dif = len(long) - len(short)
    res = []
    for ofs in range(dif + 1):
        fit = [0] * ofs + short + [N] * (dif-ofs)
        res.append(sum(abs(a-b) for a, b in zip(fit, long)))
    return res

if N < 4:
    print(sum(a!=b for a,b in zip(S,T)))
else:
    # red nad blue bar pos
    sr, sb = [], []
    tr, tb = [], []
    for i in range(N-1):
        if S[i:i+2] == '01':
            sr.append(i+1)
        if S[i:i+2] == '10':
            sb.append(i+1)
        if T[i:i+2] == '01':
            tr.append(i+1)
        if T[i:i+2] == '10':
            tb.append(i+1)


    dr, db = dist(sr, tr), dist(sb, tb)
    long, short = (dr, db) if len(dr) > len(db) else db, dr
    dif = len(long) - len(short)
    res = []
    for ofs in range(dif + 1):
        res.append(min(a+b for a, b in zip(short, long[ofs:ofs+len(short)])))

    print(min(res))
