# from heapq import heappush, heapify
# from bisect import insort_left

N, Q = map(int, input().split())
INF = 10 ** 9
event, pos, D = [], {}, []
for _ in range(N):
    s, t, x = map(int, input().split())
    # append event
    event.append((s-x, 2, x))
    # delete event (first)
    event.append((t-x, 1, x))


for _ in range(Q):
    # insort_left(event, (int(input()), 3, 0))
    event.append((int(input()), 3, 0))

event.sort()

min_valid, min_val = True, INF
for ev in event:
    # work event
    time, type, x = ev
    if type == 2:
        if min_valid:
            min_val = min(min_val, x)
        pos[x] = True
        # pos.append(x)
        # heappush(pos, x)
    elif type == 1:
        del pos[x]
        min_valid = False
        # pos.remove(x)
        # heapify(pos)
    else:
        if len(pos) == 0:
            print(-1)
        else:
            if not min_valid:
                min_val = min(pos.keys())
                min_valid = True
            print(min_val)
            # print(pos[0])
