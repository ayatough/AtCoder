N, K = map(int, input().split())
A = list(map(int, input().split()))

MAXBIT = (10 ** 12).bit_length()
F = [0] * MAXBIT  # num of bit flag 1 of A's in each digit

for a in A:
    for i in range(MAXBIT):
        F[i] += a >> i & 1

small = False
ans = 0
for i in range(MAXBIT-1, -1, -1):
    if F[i] > N//2:  # X bit is 0
        ans += F[i] * 2 ** i
        if K >> i & 1:
            small = True
    elif F[i] <= N//2:  # X bit is 1
        if small or K >> i & 1:
            ans += (N - F[i]) * 2 ** i
        else:
            ans += F[i] * 2 ** i

print(ans)
