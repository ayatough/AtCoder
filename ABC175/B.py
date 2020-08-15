from collections import Counter
from itertools import combinations

N = int(input())
L = list(map(int, input().split()))
C = Counter(L)

def can_triangle(d):
    d.sort()
    a, b, c = d
    return a+b > c


def solve():
    ans = 0
    for c in combinations(C.keys(), 3):
        if can_triangle(list(c)):
            ans += C[c[0]]*C[c[1]]*C[c[2]]
    return ans

if __name__ == "__main__":
    print(solve())
