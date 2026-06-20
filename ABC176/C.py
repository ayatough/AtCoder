N = int(input())
A = list(map(int, input().split()))

def solve():
    count = 0
    tmp = A[0]
    for i in range(1, N):
        if A[i] >= tmp:
            tmp = A[i]
        else:
            count += tmp - A[i]
    return count

if __name__ == "__main__":
    print(solve())
