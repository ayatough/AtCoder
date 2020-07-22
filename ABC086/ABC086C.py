def is_possible(t0, x0, y0, t, x, y):
    dt, dm = t - t0, abs(x - x0) + abs(y - y0)
    if dt < dm:
        return False
    if (dt + dm) % 2 == 0:
        return True
    return False
n = int(input())
path = [(0, 0, 0)]
can_travel = True
for _ in range(n):
    t0, x0, y0 = path[-1]
    t, x, y = (int(i) for i in input().split())
    can_travel &= is_possible(t0, x0, y0, t, x, y)
    path.append((t, x, y))

print('Yes' if can_travel else 'No')