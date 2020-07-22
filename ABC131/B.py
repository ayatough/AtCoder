N, L = map(int, input().split())
sum = N * (2 * L + N -1) // 2

if L > 0:
    print(sum - L)
elif N + L - 1 < 0:
    print(sum - (L + N - 1))
else:
    print(sum)

