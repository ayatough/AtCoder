N = int(input())
ans = ''
if N == 0:
    ans = '0'
else:
    while N != 0:
        if N%2 == 1:
            N -= 1
            ans += '1'
        else:
            ans += '0'
        N /= -2
print(ans[::-1])
