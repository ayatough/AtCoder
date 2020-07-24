N = int(input())

def solve():
    ans = 0
    for k in range(1,N+1):
        d = N//k
        ans += k*d*(d+1)//2
    return ans

if __name__ == "__main__":
    print(solve())
