from math import factorial
N = int(input())
S = input()
MOD = 10 ** 9 + 7

LR = [True]  # Left is True
for i in range(N*2-1):
    LR += [LR[-1]] if S[i+1] != S[i] else [not LR[-1]]

valid = S[0] == S[-1] == 'B' and not LR[-1] and LR.count(True) == N

if valid:
    # calc lr combination
    cmb = 1
    cr = 0
    for i in range(N*2-1, -1, -1):
        if not LR[i]:
            cr += 1
        else:
            cmb *= cr
            cmb %= MOD
            cr -= 1

    print((factorial(N) * cmb) % MOD)
else:
    print(0)
