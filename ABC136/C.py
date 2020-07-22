N = int(input())
H = list(map(int, input().split()))

res = True
for i in range(N-1,0,-1):
    if H[i-1] > H[i] + 1:
        res = False
        break
    elif H[i-1] == H[i] + 1:
        H[i-1] -= 1

print('Yes' if res else 'No')
