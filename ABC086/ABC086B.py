def is_square(n):
    c = 1
    while True:
        if n / c == c:
            return True
        if n / c < c:
            break
        c += 1
    return False
a, b =  input().split()
c = int(a + b)
print('Yes' if is_square(c) else 'No')