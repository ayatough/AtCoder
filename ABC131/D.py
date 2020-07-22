N = int(input())
BA = []
for _ in range(N):
    a, b = map(int, input().split())
    BA.append((b, a))

BA.sort()

can = True
cum = 0
for ba in BA:
    cum += ba[1]
    if cum > ba[0]:
        can = False
        break

print('Yes' if can else 'No')
