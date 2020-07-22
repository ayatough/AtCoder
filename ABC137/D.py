from heapq import heappop, heappush
N, M = map(int, input().split())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))

AB.sort()
pq = []
j = 0
ans = 0
for i in range(1,M+1):
    while j < N:
        a, b = AB[j]
        if a > i:
            break
        heappush(pq, -b)
        j += 1
    if len(pq) == 0:
        continue
    b = heappop(pq)
    b = -b
    ans += b

print(ans)
