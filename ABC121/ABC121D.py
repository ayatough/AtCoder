# input
A, B = (int(i) for i in input().split())


# the total num of 1 at i index under a
def num_bin(a, i):
    mod = 2 ** (i+1)
    hlf = 2 ** i
    base = (a-1) // mod * hlf
    resm = max(((a-1) % mod) - hlf + 1, 0)
    return base + resm

xor = ''

max_index = len(bin(B + 1)) - 2

for i in range(max_index):
    xor = str(num_bin(A, i) % 2 ^ num_bin(B + 1, i) % 2) + xor
    
print(int(xor, 2))
