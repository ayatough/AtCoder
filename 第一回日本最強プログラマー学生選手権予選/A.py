M, D = map(int, input().split())

cnt = 0
for m in range(1, M+1):
    for d in range(10, D+1):
        d10, d1 = divmod(d, 10)
        if d10 < 2 or d1 < 2:
            continue
        if d1 * d10 == m:
            cnt += 1

print(cnt)
