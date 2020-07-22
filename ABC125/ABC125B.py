n = int(input())
vs = (int(i) for i in input().split())
cs = (int(i) for i in input().split())
# cost per performance
cps = [v - c for v, c in zip(vs, cs)]
max_ = sum(cp for cp in cps if cp > 0)
print(max_)
