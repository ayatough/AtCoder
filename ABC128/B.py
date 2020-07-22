N = int(input())
SP = []
for i in range(N):
    s, p = input().split()
    p = -int(p)
    SP.append((s, p, i+1))

SP.sort()

print('\n'.join(str(spi[2]) for spi in SP))
