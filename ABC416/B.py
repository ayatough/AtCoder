S = input().strip()

T = ""
cum = [0]

for s in S:
    if s == "#":
        cum.append(cum[-1] + 1)
    else:
        cum.append(cum[-1])

num = 0
active = -1
for i in range(len(S)):
    pre, cur = cum[i], cum[i+1]
    if pre == cur and active != pre:
        T = T + "o"
        num += 1
        active = pre
    else:
        T = T + S[i]

print(T)
