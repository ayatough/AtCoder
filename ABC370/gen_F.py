from random import randint

with open("test_F_max", "w") as f:
    N = 2*10**5
    K = randint(2, 4)
    # AMIN, AMAX = 1, 10**4
    AMIN, AMAX = 1, 10
    f.write(f"{N} {K}\n")
    for i in range(N):
        A = randint(AMIN, AMAX)
        A = A**4
        f.write(f"{A}")
        if i == N-1:
            f.write("\n")
        else:
            f.write(" ")
