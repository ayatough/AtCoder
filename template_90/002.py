import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

def possible(s):
    a, b, c = map(ord, s)
    if b == a-1 and a == c:
        return chr(b+2)
    return None

ret = []
if N % 2 == 0:
    visited = dict()
    Q = deque()
    Q.append("b"+"ab"*((N-1)//2))
    def dfs():
        q = Q.popleft()
        visited[q] = True
        ret.append(q)
        for i in range(1,N-2):
            newp = possible(q[i-1:i+2])
            if newp:
                newq = q[:i] + newp + q[i+1:]
                if newq not in visited:
                    Q.append(newq)
                    dfs()
        if len(Q) == 0:
            return
    dfs()
    ret.sort(reverse=True)

for r in ret:
    pars = "("
    for i in range(1, len(r)):
        if ord(r[i]) - ord(r[i-1]) == 1:
            pars += "("
        else:
            pars += ")"
    pars += ")"
    print(pars)
