import sys
input = sys.stdin.readline

H, W = map(int, input().split())

C = [[0] * (W+1) for _ in range(H+1)]
A = [[0] * (W+1) for _ in range(H+1)]

for h in range(H):
    L = list(map(int, input().split()))
    for w in range(W):
        A[h+1][w+1] = L[w]
        C[h+1][w+1] = L[w] + C[h][w+1] + C[h+1][w] - C[h][w]

for h in range(H):
    print(*[C[-1][w+1] - C[-1][w] + C[h+1][-1] - C[h][-1] - A[h+1][w+1] for w in range(W)])
