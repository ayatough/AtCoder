def get_divisor(n):
    '''nの約数を返す
    '''
    d = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return d

def cmb(n, r, mod):
    '''nCrを返却(modは素数であるべし)
    '''
    from functools import reduce
    r = min(n-r, r)
    if r == 0: return 1
    over = reduce(lambda x, y : x*y % mod, range(n, n-r, -1))
    under = reduce(lambda x, y : x*y % mod, range(1, r+1))
    return (over * pow(under, mod-2, mod)) % mod
