S = input()
BLOCK = S.replace('BC', 'D').replace('B', ' ').replace('C', ' ').split()

ans = 0
for block in BLOCK:
    d_index = [i for i, s in enumerate(block) if s == 'D']
    ans += sum(r - i for (i, r) in enumerate(d_index))

print(ans)
