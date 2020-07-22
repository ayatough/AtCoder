a, b = (int(i) for i in input().split())
print('Even' if a * b % 2 == 0 else 'Odd')