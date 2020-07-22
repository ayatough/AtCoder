# input
x, y, z, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

import heapq


a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

index_hstr = []
deliciouses = []
# priority queue
pq = []
heapq.heappush(pq, (-a[0] - b[0] - c[0], 0, 0, 0))
index_hstr.append((0, 0, 0))

for t in range(k):
    deli, i, j, k = heapq.heappop(pq)
    if i+1<x and (i+1, j, k) not in index_hstr:
        heapq.heappush(pq, (-a[i+1] - b[j] - c[k], i+1, j, k))
        index_hstr.append((i+1, j, k))
    if j+1<y and (i, j+1, k) not in index_hstr:
        heapq.heappush(pq, (-a[i] - b[j+1] - c[k], i, j+1, k))
        index_hstr.append((i, j+1, k))
    if k+1<z and (i, j, k+1) not in index_hstr:
        heapq.heappush(pq, (-a[i] - b[j] - c[k+1], i, j, k+1))
        index_hstr.append((i, j, k+1))
    deliciouses.append(-deli)


print('\n'.join(str(i) for i in deliciouses))
