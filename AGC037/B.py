N = int(input())
S = input()
MOD = 998244353

# make A, B, C oredesr
r, g, b = 0, 0, 0
T = {'R': 0, 'G': 0, 'B': 0}
ABC = []  # means, A: 0, B: 1, C: 2
for s in S:
    T[s] += 1
    ge = [t >= T[s] for t in T.values()].count(True)
    lt = [t < T[s] for t in T.values()].count(True)
    if ge == 1:
        ABC.append(0)
    elif lt == 0:
        ABC.append(2)
    else:
        ABC.append(1)

la, rc = 0, 0  # selectable num of left A and right C
ans = 1

# from left for A
for d in ABC:
    if d == 0:
        la += 1
    elif d == 1:
        ans *= la
        ans %= MOD
        la -= 1

# # from right for C
for d in ABC[::-1]:
    if d == 2:
        rc += 1
    elif d == 1:
        ans *= rc
        ans %= MOD
        rc -= 1

# human permutation
for i in range(1, N+1):
    ans *= i
    ans %= MOD
print(ans)
