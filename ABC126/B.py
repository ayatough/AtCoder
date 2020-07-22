S = input()
# judge
jf, jl = 0 < int(S[:2]) <= 12, 0 < int(S[2:]) <= 12

if jf and jl:
    print('AMBIGUOUS')
elif jf and not jl:
    print('MMYY')
elif not jf and jl:
    print('YYMM')
else:
    print('NA')
