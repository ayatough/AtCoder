N = int(input())
A = list(map(int, input().split()))

from bisect import bisect_left, bisect_right

def index(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None

A.sort()
check = {i: False for i in range(N)}

count = 0
for i in range(N):
    # reverse search
    i = N - i - 1
    if check[i]:
        continue
    check[i] = True
    a = A[i]
    goal = 2 ** (len(bin(a)) - 2)
    b = goal - a
    j = index(A, b)
    if j is None:
        continue
    else:
        if check[j] == True:
            continue
        check[j] = True
        count += 1

print(count)
