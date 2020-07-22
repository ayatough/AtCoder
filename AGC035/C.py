N = int(input())

def beki(n):
    return all(b == '0' for b in bin(n)[3:])

if beki(N):
    print('No')
else:
    print('Yes')
    print(1, 2)
    for i in range(2, N, 2):
        print(i, i+1)
        print(i+N, i+1+N)
        print(N+1, i+1)
        print(N+1, i+N)
    if N % 2 == 0:
        a = 2 ** (len(bin(N)[2:]) - 1)
        b = N ^ a ^ 1
        print(a+N, N)
        print(b, N*2)
