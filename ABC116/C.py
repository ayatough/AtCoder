N = int(input())
H = list(map(int, input().split()))

cnt = 0
peak = 0
prev = 0
down = False
for h in H:
    if down and h > prev:
        cnt += peak - prev
        peak = prev
        down = False
    elif h < prev:
        down = True
    peak = max(peak, h)
    prev = h
else:
    cnt += peak

print(cnt)
