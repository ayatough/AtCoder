K = int(input())
M = 10**6+1

def solve():
    count = 1
    res = 0
    c = 7 % K
    while count < M:
        res = (res * 10) % K
        res = (res + c) % K
        if res == 0:
            return count
        count += 1
    return -1

if __name__ == "__main__":
    print(solve())
