N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]

max_dist = 0
judge = []
for (x, y) in P:
    dist = abs(x) + abs(y)
    max_dist = max(max_dist, dist)
    judge.append(dist % 2 == 0)

if all(judge) or not any(judge):
    print(max_dist)
    print(*([1] * max_dist))
    for (x, y) in P:
        com = ''
        com += abs(x) * ('R' if x > 0 else 'L')
        com += abs(y) * ('U' if y > 0 else 'D')
        com += 'LR' * ((max_dist - abs(x) - abs(y)) // 2)
        print(com)
else:
    print(-1)
