def get_divisor(n):
    '''nの約数を返す
    '''
    d = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return d

FCT = [1]
for i in range(1, M+1):
    FCT.append((FCT[-1] * i)%MOD)

def pmu(n, r, mod=MOD):
    return (FCT[n] * pow(FCT[n-r], mod-2, mod)) % mod

def cmb(n, r, mod=MOD):
    return (pmu(n, r) * pow(FCT[r], mod-2, mod)) % mod
