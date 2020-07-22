from bisect import bisect_right
N = int(input())
A = list(int(input()) for _ in range(N))
INF = 10 ** 9 + 1

dp = [INF]
for a in A:
    if -a >= dp[-1]:
        dp.append(-a)
    else:
        j = bisect_right(dp, -a)
        dp[j] = -a

print(len(dp))

# V = [False for i in range(N)]
# nv = 0
# cnt = 0
# while nv < N:
#     dp = [INF]
#     for i, a in enumerate(A):
#         if V[i]:
#             continue
#         if a > dp[-1]:
#             dp.append(a)
#         else:
#             j = bisect_left(dp, a)
#             dp[j] = a
#     nv += len(dp)
#     dp.append(INF)
#     m = len(dp)
#     for i in range(N-1, -1, -1):
#         if V[i]:
#             continue
#         if dp[m-1] <= A[i] < dp[m]:
#             V[i] = True
#             m -= 1
#     cnt += 1

# print(cnt)