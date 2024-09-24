from bisect import bisect_left

N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))
CP = [0]
for p in P:
    CP.append(CP[-1] + p)

Q = int(input())

for _ in range(Q):
    L, R = map(int, input().split())
    beg = bisect_left(X, L)
    end = bisect_left(X, R+1)
    print(CP[end] - CP[beg])
