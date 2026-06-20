from random import randint

with open("test_E_max", "w") as f:
    N = 2*10**5
    f.write(f"{N}\n")
    for i in range(1,N+1):
        f.write(f"{i}")
        if i == N:
            f.write("\n")
        else:
            f.write(" ")
