from random import randint

with open("test_E_max", "w") as f:
    N = 2*10**5
    KMIN, KMAX = -10**15, 10**15
    K = randint(KMIN, KMAX)
    AMIN, AMAX = -10**9, 10**9
    f.write(f"{N} {K}\n")
    for i in range(N):
        A = randint(AMIN, AMAX)
        f.write(f"{A}")
        if i == N-1:
            f.write("\n")
        else:
            f.write(" ")
