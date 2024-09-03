N = int(input())
H = list(map(int, input().split()))

A = [
    [0, 1, 2, 3, 3],
    [0, 1, 2, 2, 2],
    [0, 1, 1, 1, 2],
]

T = 0
for h in H:
    d, m = divmod(h, 5)
    T += d*3 + A[T%3][m]

print(T)
