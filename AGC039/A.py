S = input()
K = int(input())

cont = []
n = 1
t = S[0]
for s in S[1:]:
    if s == t:
        n += 1
    else:
        cont.append(n)
        n = 1
    t = s
else:
    cont.append(n)

C = len(cont)
ans = 0
if C == 1:
    ans += (cont[0]  * K // 2)
else:
    for i in range(1, C-1):
        ans += cont[i] // 2
    ans *= K
    ans += cont[0] // 2
    ans += cont[-1] // 2
    if S[0] == S[-1]:
        ans += ((cont[0] + cont[-1]) // 2) * (K-1)
    else:
        ans += (cont[0] // 2) * (K-1)
        ans += (cont[-1] // 2) * (K-1)

print(ans)
