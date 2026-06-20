N = int(input())

S = ""
over = False
for _ in range(N):
    c, l = input().split()
    l = int(l)
    if len(S) + l > 100:
        over = True
        break
    S += c*l

print("Too Long" if over else S)
