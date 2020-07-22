from itertools import product
S = input()
N = len(S) - 1

cum = 0
for pluses in product((0,1), repeat=N):
    sl = S[:]
    for i in range(N):
        if pluses[i] == 1:
            sl = sl[:i-N] + '+' + sl[i-N:]
    cum += sum(int(elm) for elm in sl.split('+'))

print(cum)

# # def slv(pls):
# #     sum = 0
# #     for s in S:
# #         n = int(s)
# #         if pls[i] == 1:
# #             sum += 




# # 1

# # 1 1
# #   2

# # 1 1 2
# #   2 2
# #     4

# # 1 1 2 4
# #   2 2 4
# #     4 4
# #       8

# def part(S, i):
#     l = len(S)
#     n = int(S[l-i])
#     c = clut(i, l)
#     return n * c

# def clut(i, n, j=0):
#     if i == 1:
#         return 10**j * 2**(n-i)
#     else:
#         return 2**(i-2) * 10**j * 2**(n-i) + clut(i-1, n, j+1)

# print(sum(part(S, i) for i in range(1, len(S) + 1)))
