import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
A = []

def intm1(a):
    return int(a) - 1

for _ in range(N):
    A.append(deque(list(map(intm1, input().split()))))

nokori = N*(N-1)
day = 0

while nokori > 0:
    day += 1
    ng = [False] * N
    upd = False
    for i in range(N):
        if ng[i] or len(A[i]) == 0:
            continue
        j = A[i][0]
        if len(A[j]) > 0 and A[j][0] == i and not ng[j]:
            ng[A[i].popleft()] = True
            ng[A[j].popleft()] = True
            upd = True
            nokori -= 2
    if not upd:
        break

print(day if nokori == 0 else -1)
