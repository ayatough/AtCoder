A, B, C = map(int, input().split())

if B < A < C or A < C < B or C < B < A:
    print("No")
else:
    print("Yes")
