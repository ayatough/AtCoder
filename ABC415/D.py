N, M = map(int, input().split())

AB = []
for _ in range(M):
    AB.append(tuple(map(int, input().split())))

AB.sort(key=lambda x: (x[0] - x[1], x[0]))

ans = 0
n = N
for a, b in AB:
    if n >= a:
        c = a - b
        m = (n - a) // c + 1
        ans += m
        n -= m * c

print(ans)
