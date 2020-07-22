E = list(map(int, input().split()))
B = int(input())
L = list(map(int, input().split()))


# m = list(e == l for (e, l) in zip(E, L)).count(True) # match
for i in 

if m == 6:
    print(1)
elif m == 5:
    v = sum(l for (e, l) in zip(E, L) if e != l)
    if v == B:
        print(2)
    else:
        print(3)
elif m == 4:
    print(4)
elif m == 3:
    print(5)
else:
    print(0)
