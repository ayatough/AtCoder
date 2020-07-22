# input
h, w = [int(i) for i in input().split()]
ary = []
for y in range(h):
    line = input()
    ary.append(line)

max_val = pow(10, 6)

def convert_ary(ary):
    # #. -> 0, 1, 2
    tmp = [[] for i in range(w)]
    for y in range(h):
        for x in range(w):
            tmp[y].append(None if ary[y][x] == '.' else 0)

    return tmp

ary = convert_ary(ary)

def upd_left(ary, y, x):
    if x == 0:
        return ary
    if ary[y][x-1] is None:
        ary[y][x-1] = ary[y][x] + 1
    else:
        ary[y][x-1] = min(ary[y][x-1], ary[y][x] + 1)
    return ary

def upd_right(ary, y, x):
    if x == w - 1:
        return ary
    if ary[y][x+1] is None:
        ary[y][x+1] = ary[y][x] + 1
    else:
        ary[y][x+1] = min(ary[y][x+1], ary[y][x] + 1)
    return ary

def upd_up(ary, y, x):
    if y == 0:
        return ary
    if ary[y-1][x] is None:
        ary[y-1][x] = ary[y][x] + 1
    else:
        ary[y-1][x] = min(ary[y-1][x], ary[y][x] + 1)
    return ary

def upd_down(ary, y, x):
    if y == h - 1:
        return ary
    if ary[y+1][x] is None:
        ary[y+1][x] = ary[y][x] + 1
    else:
        ary[y+1][x] = min(ary[y+1][x], ary[y][x] + 1)
    return ary

# from copy import deepcopy

def update_ary(ary):
    # tmp = deepcopy(ary)
    for y in range(h):
        for x in range(w):
            if ary[y][x] is None:
                continue
            ary = upd_left(ary, y, x)
            ary = upd_right(ary, y, x)
            ary = upd_up(ary, y, x)
            ary = upd_down(ary, y, x)
    return ary

def is_complete(ary):
    for line in ary:
        if None in line:
            return False
    return True

while not is_complete(ary):
    ary = update_ary(ary)

print(max(elem for line in ary for elem in line))
