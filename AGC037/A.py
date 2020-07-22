S = input()
N = len(S)

ans = 0
prev = ''
cur = ''
for s in S:
    cur += s
    if prev == cur:
        continue
    ans += 1
    prev = cur
    cur = ''

print(ans)
