from collections import Counter
N = int(input())

CL = []
for _ in range(N):
    s = [c for c in input()]
    s.sort()
    CL.append(''.join(s))

CL.sort()

num = 0
ans = 0
for i in range(1,N):
    if CL[i] == CL[i-1]:
        num += 1
    else:
        ans += num * (num + 1) // 2
        num = 0
ans += num * (num + 1) // 2

print(ans)
