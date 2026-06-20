N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

ia = 0
ib = 0

count = 0

while ia < N and ib < M:
    a = A[ia]
    b = B[ib]
    if b > 2 * a:
        ib += 1
        continue
    ia += 1
    ib += 1
    count +=1

print(count)
