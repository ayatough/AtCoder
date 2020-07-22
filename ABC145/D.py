from functools import reduce
X, Y = map(int, input().split())
MOD = 10**9 + 7

def cmb(n, r, mod):
    '''nCrを返却(modは素数であるべし)
    '''
    r = min(n-r, r)
    if r == 0: return 1
    over = reduce(lambda x, y : x*y % mod, range(n, n-r, -1))
    under = reduce(lambda x, y : x*y % mod, range(1, r+1))
    return (over * pow(under, mod-2, mod)) % mod

if 2*Y-X < 0 or 2*X-Y < 0 or (2*Y-X)%3 != 0 or (2*X-Y)%3 != 0:
    print(0)
else:
    a, b = (2*X-Y)//3, (2*Y-X)//3
    print(cmb(a+b, a, MOD))
