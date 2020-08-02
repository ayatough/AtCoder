N, D = map(int, input().split())
DD = D*D

def solve():
    count = 0
    for _ in range(N):
        x, y = map(int, input().split())
        if x**2 + y**2 <= DD:
            count += 1
    return count

if __name__ == "__main__":
    print(solve())
