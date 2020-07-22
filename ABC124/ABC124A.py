# input
a, b = (int(i) for i in input().split())
print(max(a * 2 - 1, b * 2 - 1, a + b))
