N = int(input())

T = [9, 900, 90000]
L = len(str(N))

ans = sum(T[i] for i in range(L//2))
if L % 2 == 1:
    ans += N - (10 ** (L-1)) + 1

print(ans)
