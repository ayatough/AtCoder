N = int(input())
S = input()

def search(c, text):
    pos = -1
    for i, s in enumerate(text):
        if s == c:
            pos = i
            break
    return pos

cnt = 0
for i in range(10):
    ip = search(str(i), S[0:])
    if ip < 0:
        continue
    for j in range(10):
        jp = search(str(j), S[ip+1:])
        if jp < 0:
            continue
        for k in range(10):
            kp = search(str(k), S[ip+jp+2:])
            if kp < 0:
                continue
            cnt += 1

print(cnt)
