L, R = map(int, input().split())

if L + R == 0 or L + R == 2:
    print("Invalid")
else:
    print("Yes" if L == 1 else "No")
