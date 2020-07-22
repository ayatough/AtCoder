def fullfill(k, x, y, c):
    return (x < k) ^ (y < k)
n, k = (int(i) for i in input().split())
xyc = []
for i in range(n):
    x, y, c = input().split()
    xyc.append((int(x), int(y), c))
kibou = []
k2 = k * 2
for xr in range(k2):
    for yr in range(k2):
        kibou.append(sum(fullfill(k, (x + xr) % k2, (y + yr) % k2, c) for x, y, c in xyc))
print(max(kibou))
