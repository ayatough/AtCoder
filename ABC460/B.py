T = int(input())

answers = []
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dx2 = (x1 - x2)**2
    dy2 = (y1 - y2)**2
    sr2 = (r1 + r2)**2
    dr2 = (r1 - r2)**2
    is_ok = dr2 <= dx2 + dy2 <= sr2
    answers.append("Yes" if is_ok else "No")

for ans in answers:
    print(ans)
