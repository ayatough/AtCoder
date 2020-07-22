from itertools import product, accumulate
S = input()

def eval_(s, pat):
    s = list(map(int, s))
    ans = s[0]
    for i in range(3):
        if pat[i] == '+':
            ans += s[i+1]
        else:
            ans -= s[i+1]
    return ans

eq = ''
for pat in product(('+', '-'), repeat=3):
    if eval_(S, pat) == 7:
        eq = S[0]
        for i in range(3):
            eq += pat[i] + S[i+1]
        break

print(eq+'=7')
