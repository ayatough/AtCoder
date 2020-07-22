N, K = map(int, input().split())
print((N//K)**3 + (((N+K//2)//K)**3 if K%2 == 0 else 0))
