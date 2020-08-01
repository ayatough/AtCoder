M = 10**6
N = int(input())
A = list(map(int, input().split()))


def solve():
    amax = max(A)+1
    memo = [0] * amax
    for a in A:
        i = 1
        while i*a < amax:
            memo[i*a] += 1
            i += 1

    count = 0
    for a in A:
        if memo[a] == 1:
            count += 1

    return count

if __name__ == "__main__":
    print(solve())
