from collections import deque
N = int(input())
A = [int(i) for i in input().split()]

pos = [a for a in A if a >= 0]
neg = [a for a in A if a < 0]
# zero = [a for a in A if a == 0]

pos.sort()
neg.sort()

pd = deque(pos)
nd = deque(neg)

buf = []

while len(pd) + len(nd) > 2:  # more 3
    # もし負の数が無かったら追加
    if len(nd) == 0:
        y, x = pd.pop(), pd.popleft()
        buf.append((x, y))
        nd.append(x - y)
        continue
    # もし正の数が無かったら追加
    if len(pd) == 0:
        x, y = nd.pop(), nd.popleft()
        buf.append((x, y))
        pd.append(x - y)
        continue
    # 正の数が1より大きかったら減らす
    if len(pd) > 1:
        x, y = nd.pop(), pd.pop()
        buf.append((x, y))
        nd.append(x - y)
        continue
    # 正の数がちょうど1だったらどんどん正の数を大きくする
    if len(pd) == 1:
        x, y = pd.pop(), nd.pop()
        buf.append((x, y))
        pd.append(x - y)
        continue

merge = []
merge.extend(nd)
merge.extend(pd)

val = merge[1] - merge[0]
buf.append((merge[1], merge[0]))

# print
print(val)
for b in buf:
    print(b[0], b[1])