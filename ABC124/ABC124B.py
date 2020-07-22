# input
n = int(input())
hs = tuple(int(i) for i in input().split())

count = 0
for i, h in enumerate(hs):
    if all(hh <= h for hh in hs[:i]):
        count += 1

print(count)
