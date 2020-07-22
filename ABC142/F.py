import sys
from collections import deque
sys.setrecursionlimit = 10 ** 9
N, M = map(int, input().split())
V = {i: [] for i in range(1,N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    V[a].append(b)
INF = float('inf')

def get_cycle(s):
    H = deque()
    seen = {i: False for i in range(1,N+1)}
    finished = {i: False for i in range(1,N+1)}
    last = [0]
    def dfs(u):
        H.append(u)
        seen[u] = True
        for v in V[u]:
            if finished[v]:
                continue
            if seen[v] and not finished[v]:
                last[0] = v
                return
            dfs(v)
            if last[0]:
                return
        H.pop()
        finished[u] = True
    
    dfs(s)
    cycle = []
    while H:
        cycle.append(H.pop())
        if cycle[-1] == last[0]:
            break
        
    return cycle[::-1]

ans = get_cycle(1)

has_smaller_cycle = True
while has_smaller_cycle:
    has_smaller_cycle = False
    for i in range(len(ans)):
        for v in V[ans[i]]:
            if v != ans[(i+1)%len(ans)]:
                if v in ans:
                    short_cut = (i, ans.index(v))
                    has_smaller_cycle = True
                    break
        if has_smaller_cycle:
            break
    if has_smaller_cycle:
        a, b = short_cut
        if a < b:
            ans = ans[:a+1] + ans[b:]
        else:
            ans = ans[b:a+1]

if len(ans):
    print(len(ans))
    for a in ans:
        print(a)
else:
    print(-1)
