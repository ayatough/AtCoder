X = input().strip()

while X[-1] in ["0", "."]:
    if X[-1] == ".":
        X = X[:-1]
        break
    X = X[:-1]

print(X)
