M = 10**6
N = int(input())
A = list(map(int, input().split()))


def solve():
    memo = [0] * M
    for a in A:
        i = 1
        while i*a < M:
            memo[i*a] += 1
            i += 1

    count = 0
    for a in A:
        if memo[a] == 1:
            count += 1

    return count

if __name__ == "__main__":
    print(solve())
