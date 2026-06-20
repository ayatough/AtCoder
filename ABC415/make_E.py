import random
random.seed(42)

with open("test_E_hand", "w") as f:
    H = 5
    W = 5
    f.write(str(H) + " " + str(W) + "\n")

    for y in range(H):
        A = []
        for x in range(W):
            A.append(str(random.randint(0, 50)))
        f.write(" ".join(A) + "\n")

    P = []
    for i in range(H + W - 1):
        P.append(str(random.randint(0, 50)))

    f.write(" ".join(P) + "\n")
