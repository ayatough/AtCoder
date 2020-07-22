N = int(input())
S = input()
ans = 1
p = S[0]
for s in S[1:]:
    if s == p:
        continue
    ans += 1
    p = s
print(ans)
