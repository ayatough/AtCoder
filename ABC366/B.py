N = int(input())
M = []

m = 0
for i in range(N):
    s = input().strip()
    M.append(s + "*" * (100 - len(s)))
    m = max(m, len(s))

for i in range(m):
    s = ""
    for j in range(N):
        s = M[j][i] + s
    print(s.rstrip("*"))
