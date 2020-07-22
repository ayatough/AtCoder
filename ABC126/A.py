N, K = map(int, input().split())
S = input()
res = ''
for i, s in enumerate(S):
    if i == K - 1:
        res += s.lower()
    else:
        res += s
print(res)
