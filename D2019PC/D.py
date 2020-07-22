# input
N = int(input())

# n = a * b + b
#   = b * (a + 1)
# b < a < sqrt(n)

import math
# square cut
sqnc = int(math.sqrt(N))

print(sum(N // b - 1 for b in range(1, sqnc+1) if N % b == 0 and b < N // b -1))
