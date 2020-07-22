N, A, B, C, D = map(int, input().split())
S = input()

def yn(a):
    print('Yes' if a else 'No')

if C < D:
    # `##` is NG btw A and D
    yn('##' not in S[A:C] and '##' not in S[B:D])
else:
    # `#` is NG prev D except oikoseru
    yn('##' not in S[A:C] and '...' in S[B-2:D+1])
