import fractions
import itertools

n = int(input())
as_ = [int(i) for i in input().split()]


def gcds(list_):
    return list(itertools.accumulate(list_, fractions.gcd))


def reversed_gcds(list_):
    return list(itertools.accumulate(reversed(list_), fractions.gcd))

at
as_accum_gcd, as_rev_accum_gcd = gcds(as_), reversed_gcds(as_)

dropped_gcds = []
for i in range(len(as_)):
    if i == 0:
        dropped_gcd = as_rev_accum_gcd[-2]
    elif i == len(as_) - 1:
        dropped_gcd = as_accum_gcd[-2]
    else:
        dropped_gcd = fractions.gcd(as_accum_gcd[i - 1], as_rev_accum_gcd[-2 - i])
    dropped_gcds.append(dropped_gcd)

print(max(dropped_gcds))
