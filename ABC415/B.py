S = input().strip()

buf = []
for i, s in enumerate(S):
    if s == ".":
        continue
    elif s == "#":
        buf.append(i+1)
        if len(buf) == 2:
            print(*buf, sep=",")
            buf = []
