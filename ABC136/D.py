S = input()
N = len(S)

round = lambda x:int((x*2+1)//2)
ans = []
r, l = 0, 0
for i in range(N):
    if i == N-1 or S[i:i+2] == 'LR':
        l += 1
        ans.append([0] * (r-1) + [round(r/2) + l//2, round(l/2) + r//2] + [0] * (l-1))
        r, l = 0, 0
    else:
        if S[i] == 'R':
            r += 1
        elif S[i] == 'L':
            l += 1

print(' '.join(' '.join(str(e) for e in elem) for elem in ans))
