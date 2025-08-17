A = int(input())
N = int(input())

def judge(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

def to_base(n, A):
    s = ""
    while n:
        s += str(n%A)
        n //= A
    return s

ans = 0
M = 10**((len(str(N))+1)//2) - 1
for m in range(1, M+1):
    m = str(m)
    n = int(m[:] + m[::-1])
    if n <= N and judge(to_base(n, A)):
        ans += n

    n = int(m[:-1] + m[::-1])
    if n <= N and judge(to_base(n, A)):
        ans += n

print(ans)
