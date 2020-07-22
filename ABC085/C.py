N, Y = map(int, input().split())

v = 0
def solve():
    for x in range(N+1):
        if Y // 10000 < x:
            return [-1,-1,-1]
        r = Y - 10000 * x
        for y in range(0, r // 5000 + 1):
            rr = r - 5000 * y
            z = rr // 1000
            if x + y + z == N:
                return [x, y, z]
    return [-1,-1,-1]

print(' '.join(map(str, solve())))
