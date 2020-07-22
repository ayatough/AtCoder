A, B, X = map(int, input().split())
lo, hi = 0, 10**9+1
while lo < hi - 1:
    mi = (lo+hi)//2
    price = A*mi + len(str(mi)) * B
    if price <= X:
        lo = mi
    else:
        hi = mi
print(lo)
