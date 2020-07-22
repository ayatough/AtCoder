n,q,*t=map(int,open(0).read().split())
e=[[]for _ in[0]*n]
s=[0]
d=s*n
f=[1]+s*n
for a,b in zip(*[iter(t[:-q-q])]*2):
  e[a-1]+=b-1,
  e[b-1]+=a-1,
for p,x in zip(*[iter(t[-q-q:])]*2):d[p-1]+=x
while s:
  v=s.pop()
  for w in e[v]:
    if f[w]:continue
    f[w]=1
    d[w]+=d[v]
    s+=w,
print(*d)
