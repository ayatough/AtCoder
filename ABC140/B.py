N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

scr = sum(B)
for i in range(1,N):
    if A[i] == A[i-1] + 1:
        scr += C[A[i]-2]

print(scr)
