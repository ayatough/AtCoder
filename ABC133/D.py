N = int(input())
A = list(map(int, input().split()))

B = [sum((a if i % 2 == 0 else -a) for (i, a) in enumerate(A))]
for i in range(N-1):
    B.append(2*A[i]-B[-1])

print(' '.join(map(str, B)))
