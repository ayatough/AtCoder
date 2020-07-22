N, M = map(int, input().split())

def get_divisor(n):
    '''nの約数を返す
    '''
    d = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return d

D = list(get_divisor(M))
D.sort(reverse=True)

ans = 0
for d in D:
    if M//d < N:
        continue
    ans = d
    break

print(ans)
