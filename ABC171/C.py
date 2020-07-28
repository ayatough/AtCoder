N = int(input()) - 1

def solve():
    ans = ''
    res = N
    q = 26
    while q > 0:
        q, r = divmod(res, 26)
        res = q-1
        ans = chr(ord('a') + r) + ans
    return ans

if __name__ == "__main__":
    print(solve())
