N = int(input())

M = 998244353

def solve(N):
    cnt = N
    prev = N
    ans = (1+N)*N//2 - prev
    cnt -= 1
    i = 2
    while cnt > 0:
        curr = N // i
        ans -= curr
        cnt -= 1
        res = prev - curr
        if cnt > 0 and i < curr:
            ans -= res * (i-1)
            cnt -= res
            prev = curr
        i += 1

    return ans % M

print(solve(N))

# def cal2(N):
#     ans2 = (1+N)*N//2

#     for i in range(1, N+1):
#         # if N == 20:
#         #     print(i, N//i)
#         ans2 -= N // i

#     return ans2

# print(ans2)

# for i in range(3, N+1):
#     c1 = cal1(i)
#     c2 = cal2(i)
#     if c1 != c2:
#         print(i, c1, c2)
