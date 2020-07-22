L = input()
MOD = 10 ** 9 + 7

N = len(L)
one = 0
for i in range(N):
    if L[i] == '1':
        one += int(((N-1-i) * 2**(N-i-2))) % MOD
        if i != N-1:
            one += (int(L[(i+1):]) + 1) % MOD
        else:
            one += 1

print((one*2+1) % MOD)
