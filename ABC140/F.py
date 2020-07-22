N = int(input())
S = list(map(int, input().split()))

S.sort()
def compress(s):
    n = (len(s)-1).bit_length()
    j = 0
    comp = [0] * (2 ** n)
    comp[j] += 1
    for i in range(1,2**n):
        if s[i] > s[i-1]:
            j += 1
        comp[j] += 1
    return comp, j

comp, m = compress(S)

valid = True
for i in range(N):
    k = 0
    l = 1
    if l >= len(comp) or comp[l] == 0:
        valid = False
        break
    
    news = []
    for j in range(2**(N-i-1)):
        comp[k] -= 1
        comp[l] -= 1
        news.append(l)
        if not comp[l]:
            if not comp[k]:
                k = l + 1
                l += 2
            else:
                l += 1
        else:
            if not comp[k]:
                k = l
                l += 1
            else:
                pass
        if l > m:
            break
    if j < 2**(N-i-1) - 1:
        break
    comp, m = compress(news)
if i < N - 1:
    valid = False

print('Yes' if valid else 'No')
