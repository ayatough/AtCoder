N = int(input())
A = list(map(int, input().split()))
A = [a - i - 1 for (a, i) in enumerate(A)]
A.sort()
med = A[N//2]
print(sum(abs(a-med) for a in A))