# input
N, MOD = int(input()), 10 ** 9 + 7


memo = [{} for _ in range(N+1)]


# check validity
def ok(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i-1], t[i] = t[i], t[i-1]
        if ''.join(t).count('AGC') >= 1:
            return False
    return True


def dfs(cur, last3):
    if last3 in memo[cur]:
        return memo[cur][last3]
    if cur == N:
        return 1
    ret = 0
    # append any char
    for c in 'ACGT':
        if ok(last3 + c):
            ret = (ret + dfs(cur + 1, last3[1:] + c)) % MOD
    memo[cur][last3] = ret
    return ret

# print(dfs(0, '...'))
# def judge(s):
#     last4 = s[-4:]


# ncase(0) == 1
# ncase(1) == 4

# def ncase(l):
#     for c in 'ACGT':
#         ncase(l[-3:] + c)

memo = [{} for _ in range(N+1)]


def ncase(n, last3='...'):
    if last3 in memo[n]:
        return memo[n][last3]
    if n == 0:
        return 1
    ret = 0
    for c in 'ACGT':
        if ok(last3 + c):
            ret = (ret + ncase(n - 1, last3[1:] + c)) % MOD
    memo[n][last3] = ret
    return ret

print(ncase(N))



pass
