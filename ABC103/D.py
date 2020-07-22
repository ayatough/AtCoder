N, M = map(int, input().split())
BA = []
for _ in range(M):
    a, b = map(int, input().split())
    BA.append((b, a))

BA.sort()

cnt = 0
end = 0
for ba in BA:
    b, a = ba
    if a > end:
        cnt += 1
        end = b - 1

print(cnt)
