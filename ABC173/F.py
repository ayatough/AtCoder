N = int(input())

def solve():
    nedge = 0
    npoint = N*(N+1)*(N+2)//6
    for _ in range(N-1):
        u, v = map(int, input().split())
        u, v = min(u, v), max(u, v)
        nedge += u * (N-v+1)
    return npoint - nedge


if __name__ == "__main__":
    print(solve())
