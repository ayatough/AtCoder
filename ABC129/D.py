H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input()

_hor, _ver = [[None for _ in range(W)] for _ in range(H)], [[None for _ in range(W)] for _ in range(H)]

def hor(x, y):
    if _hor[y][x] is not None:
        return _hor[y][x]
    if S[y][x] == '#':
        _hor[y][x], _ver[y][x] = 0
        return 0
    cnt = 0
    pos = x - 1
    cur = S[y][pos]
    while cur == '.' and pos >= 0:
        cnt += 1
        cur = S[y][pos]
        pos -= 1
    pos = x + 1
    cur = S[y][pos]
    while cur == '.' and pos < W:
        cnt += 1
        cur = S[y][pos]
        pos += 1
    _

        




for y in range(H):
