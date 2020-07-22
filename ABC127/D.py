N, M = map(int, input().split())
A = list(map(int, input().split()))
CB = []
for _ in range(M):
    b, c = map(int, input().split())
    CB.append((c, b))

# ascend
A.sort()

# descend
CB.sort(reverse=True)

# fill convert ary
conv = []
for cb in CB:
    c, b = cb
    conv.extend([c] * b)
    if len(conv) >= N:
        break

cl = len(conv)

sum = 0
for i in range(N):
    if i >= cl:
        sum += A[i]
    else:
        sum += max(A[i], conv[i])

print(sum)
