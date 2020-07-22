from heapq import heappop, heappush, heapify
N = int(input())
V = list(map(int, input().split()))

V.sort()

heapify(V)

for i in range(N-1):
    a = heappop(V)
    b = heappop(V)
    heappush(V, (a+b)/2)

ans = heappop(V)

print(ans)
