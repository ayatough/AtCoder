from fractions import gcd
N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = abs(A[0] - X)

for x in A[1:]:
    ans = gcd(ans, abs(x - X))
    if ans == 1:
        break

print(ans)