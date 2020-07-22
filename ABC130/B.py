N, X = map(int, input().split())
L = list(map(int, input().split()))

cum = 0
cnt = 0
for l in L:
    if cum > X:
        break
    cnt += 1
    cum += l

if cum <= X:
    cnt += 1

print(cnt)
