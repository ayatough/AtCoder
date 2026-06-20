N, L, R = map(int, input().split())

cnt = 0
for _ in range(N):
    X, Y = map(int, input().split())
    cnt += X <= L and R <= Y

print(cnt)
