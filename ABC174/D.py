N = int(input())
C = input()

def solve():
    red = C.count('R')
    white = C[:red].count('W')
    return white

if __name__ == "__main__":
    print(solve())
