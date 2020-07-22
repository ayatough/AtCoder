# input
h, w = [int(i) for i in input().split()]
ary = []
for y in range(h):
    ary.append([None if i == '.' else 0 for i in input()])


from collections import deque

update_q = deque((y, x) for y, line in enumerate(ary) for x, elem in enumerate(line) if elem == 0)

def update(ary, update_q):
    for _ in range(len(update_q)):
        pos = update_q.popleft()
        y, x = pos
        if x > 0:
            uy, ux = y, x-1
            if ary[uy][ux] is None:
                ary[uy][ux] = ary[y][x] + 1
                update_q.append((uy, ux))
        if x < w-1:
            uy, ux = y, x+1
            if ary[uy][ux] is None:
                ary[uy][ux] = ary[y][x] + 1
                update_q.append((uy, ux))
        if y > 0:
            uy, ux = y-1, x
            if ary[uy][ux] is None:
                ary[uy][ux] = ary[y][x] + 1
                update_q.append((uy, ux))
        if y < h-1:
            uy, ux = y+1, x
            if ary[uy][ux] is None:
                ary[uy][ux] = ary[y][x] + 1
                update_q.append((uy, ux))
    return ary, update_q


black_count = len(update_q)
update_count = 0
while black_count < w * h:
    ary, update_q = update(ary, update_q)
    black_count += len(update_q)
    update_count += 1


print(update_count)

# def init_ary(ary):
#     # #. -> 0, 1, 2
#     tmp = [[] for i in range(w)]
#     for y in range(h):
#         for x in range(w):
#             tmp[y].append(1 if ary[y][x] == '.' else 0)
#     return tmp


# def is_all_black(ary):
#     return not any(1 in line for line in ary)

# ary = init_ary(ary)

# count = 0

# while not is_all_black(ary):
#     ary = update(ary)
#     count += 1

# print(count)
