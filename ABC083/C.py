X, Y = map(int, input().split())
cur = X
cnt = 0
while cur <= Y:
    cur <<= 1
    cnt += 1
print(cnt)
