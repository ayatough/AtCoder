K, S = map(int, input().split())

ans = 0
for x in range(min(K+1, S+1)):
    if K < (S - x) //2:
        ans +=  0
    elif K < (S - x):
        ans += K * 2 - (S - x) + 1
    else:
        ans += (S - x) + 1

print(ans)
