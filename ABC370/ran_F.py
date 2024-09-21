from random import randint

with open("test_F_ran", "w") as f:
    NMAX = 30
    N = randint(2, NMAX)
    K = randint(2, N)
    AMIN, AMAX = 2, 10**4
    f.write(f"{N} {K}\n")
    for i in range(N):
        A = randint(AMIN, AMAX)
        # A = 1
        # A = randint(0, 1)
        # A = (1 if A == 0 else 10**4)
        f.write(f"{A}")
        if i == N-1:
            f.write("\n")
        else:
            f.write(" ")
