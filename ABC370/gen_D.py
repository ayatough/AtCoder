from random import randint

with open("test_D_max", "w") as f:
    Q = 2*10**5
    H = 4*100
    W = 10*100
    f.write(f"{H} {W} {Q}\n")
    for _ in range(Q):
        f.write(f"{randint(1,H)} {randint(1,W)}\n")
