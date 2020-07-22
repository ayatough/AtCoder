h, w, n = [int(i) for i in input().split()]
sr, sc = [int(i) for i in input().split()]
s = input()
t = input()


dpx = [None for _ in range(n*2+1)]
dpy = [None for _ in range(n*2+1)]

dpx[0] = (1, w+1)
dpy[0] = (1, h+1)

# search safety region from tail
for i in range(1,n*2+1):
    is_t = i % 2 == 1
    strategy = t[-1-(i-1)//2] if is_t else s[-1-(i-1)//2]

    # T's turn: want to expand region
    if is_t:
        if strategy == 'L':
            dpx[i] = (dpx[i-1][0], min(dpx[i-1][1] + 1, w+1))
            dpy[i] = dpy[i-1]
        if strategy == 'R':
            dpx[i] = (max(1, dpx[i-1][0] - 1), dpx[i-1][1])
            dpy[i] = dpy[i-1]
        if strategy == 'U':
            dpy[i] = (dpy[i-1][0], min(dpy[i-1][1] + 1, h+1))
            dpx[i] = dpx[i-1]
        if strategy == 'D':
            dpy[i] = (max(1, dpy[i-1][0] - 1), dpy[i-1][1])
            dpx[i] = dpx[i-1]
    # S's turn: want to contract region
    else:
        if strategy == 'L':
            dpx[i] = (dpx[i-1][0] + 1, dpx[i-1][1])
            dpy[i] = dpy[i-1]
        if strategy == 'R':
            dpx[i] = (dpx[i-1][0], dpx[i-1][1] - 1)
            dpy[i] = dpy[i-1]
        if strategy == 'U':
            dpy[i] = (dpy[i-1][0] + 1, dpy[i-1][1])
            dpx[i] = dpx[i-1]
        if strategy == 'D':
            dpy[i] = (dpy[i-1][0], dpy[i-1][1] - 1)
            dpx[i] = dpx[i-1]
    # safety region has been cotrancted to 0, then break
    if len(range(*dpx[i])) == 0 or len(range(*dpy[i])) == 0:
        break

print('NO' if dpx[-1] is None else 'YES' if sr in range(*dpy[-1]) and sc in range(*dpx[-1]) else 'NO')
