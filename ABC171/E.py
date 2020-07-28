from functools import reduce
from operator import xor

N = int(input())
A = list(map(int, input().split()))

def solve():
    tot = reduce(xor, A, 0)
    return ' '.join(map(str, [a ^ tot for a in A]))

if __name__ == "__main__":
    print(solve())
