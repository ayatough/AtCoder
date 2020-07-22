N, X = map(int, input().split())

pos = X
eat = 0
for i in range(N-1, -1, -1):
    nlayer = 2 ** (i+2) - 3
    npatie = 2 ** (i+1) - 1
    if pos == 1:
        break
    elif pos <= 1 + nlayer:
        pos -= 1
        if i == 0:
            eat += 1
        continue
    elif pos == 2 + nlayer:
        eat += npatie + 1
        break
    elif pos <= nlayer * 2 + 2:
        eat += npatie + 1
        if i == 0:
            eat += 1
        pos -= nlayer + 2
    else:
        eat += npatie * 2 + 1
        break

print(eat)
