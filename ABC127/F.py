Q = int(input())
INF = 10 ** 9

queries = []
for _ in range(Q):
    queries.append(input())

from bisect import insort_left
from heapq import heappush, heappop

absum, bsum, c = 0, 0, 0
# left, right = -INF, INF
lefts, rights = [INF], [INF]
for query in queries:
    if query[0] == '2':
        # absum = sum(abs(a - ary[(c-1)//2]) for a in ary)
        # absum = asum - (c//2 + 1) * ary[(c-1)//2]
        # print(' '.join(map(str, (ary[(c-1)//2], absum + bsum))))
        # print(str(ary[(c-1)//2]) + ' ' + str(absum + bsum))
        print(-lefts[0], absum + bsum)
    else:
        _, a, b = map(int, query.split())
        if c % 2 == 0:
            if -lefts[0] <= a <= rights[0]:
                heappush(lefts, -a)
                heappush(rights, a)
                absum += 0
            elif a < -lefts[0]:
                heappush(lefts, -a)
                heappush(rights, -lefts[0])
                absum += -lefts[0] - a
            else:
                heappush(rights, a)
                heappush(lefts, -rights[0])
                absum += a - rights[0]
        else:
            if a < -lefts[0]:
                absum += -lefts[0] - a
                heappop(lefts)
                heappush(lefts, -a)
            else:
                absum += a - rights[0]
                heappop(rights)
                heappush(rights, a)
        # left, right = ary[(c-1)//2], ary[c - (c-1)//2 - 1]        
        bsum += b
        c += 1
