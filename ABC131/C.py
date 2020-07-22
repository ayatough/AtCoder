from fractions import gcd
A, B, C, D = map(int, input().split())

cmul = (B // C) - ((A - 1) // C)
dmul = (B // D) - ((A - 1) // D)
CD = C * D // gcd(C, D)
cdmul = (B // CD) - ((A - 1) // CD)

print((B - A + 1) - (cmul + dmul - cdmul))
