S = input()

if S.find("RRR") >= 0:
    print(3)
elif S.find("RR") >= 0:
    print(2)
elif S.find("R") >= 0:
    print(1)
else:
    print(0)
