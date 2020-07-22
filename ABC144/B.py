N = int(input())
valid = False
for i in range(1,10):
    if N%i == 0:
        if N//i < 10:
            valid = True
            break
print('Yes' if valid else 'No')