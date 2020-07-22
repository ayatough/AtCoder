N = int(input())
I = [0] * N
A = list(map(int, input().split()))
for i, a in enumerate(A):
    I[a-1] = i+1
print(*I)
