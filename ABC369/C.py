N = int(input())
A = list(map(int, input().split()))

num = 0
best = 0

for i in range(N):
    if i > 1:
        if A[best] - A[best+1] != A[i-1] - A[i]:
            best = i - 1

    num += i - best + 1

print(num)
