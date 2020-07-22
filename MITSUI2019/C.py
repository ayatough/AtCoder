X = int(input())
n = ((X % 100)-1) // 5
print(0 if n >= X // 100 else 1)
