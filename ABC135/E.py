K = int(input())
X, Y = map(int, input().split())

if K % 2 == 0 and (abs(X) + abs(Y)) % 2 != 0:
    print(-1)
else:
    mx, my = max(abs(X), abs(Y)), min(abs(X), abs(Y))  # modified by symmetry
    ax, ay = mx // K, my // K  # axial path count
    bx, by = mx % K, my % K  # base point
    P = []  # path
    if bx + by == 0:  # reach only axial path
        pass
    elif bx + by == K:  # reach directly to base
        P.append((bx, by))
    else:
        do_back = False
        # even K: [start] -> [dist == K point] -> [all near even point] (never reach odd point)
        if K % 2 == 0:
            if ax > 0 and (bx + by) < K:  # think K < bx + by < 2K region
                bx += K
        # odd K: [start] -> [dist == K point] -> [all near even point] -> [all near odd point]
        else:
            if bx + by < K:
                bx += K
            if (bx + by) % 2 != 0:
                if ax == 0:
                    do_back = True
                bx += K
        fx = (bx - by) // 2  # first path x
        fy = K - fx  # first path y
        P.append((fx, fy))
        P.append((bx, by))
        if do_back:
            P.append((bx - K, by))

    for x in range(bx, mx, K):
        P.append((x + K, by))
    for y in range(by, my, K):
        P.append((mx, y + K))

    print(len(P))
    do_rotate = mx != abs(X)
    do_flip_x = X < 0
    do_flip_y = Y < 0
    sgnx = -1 if do_flip_x else 1
    sgny = -1 if do_flip_y else 1
    for p in P:
        if not do_rotate:
            print(p[0] * sgnx, p[1] * sgny)
        else:
            print(p[1] * sgnx, p[0] * sgny)
