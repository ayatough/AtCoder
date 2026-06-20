import random
random.seed(42)

max_N = 18

with open("test_C_hand", "w") as f:
    f.write(str(1) + "\n")
    f.write(str(max_N) + "\n")
    s = ""
    for i in range((1 << max_N) - 1):
        s += str(random.randint(0, 1))
    f.write(s + "\n")
