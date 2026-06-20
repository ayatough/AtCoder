import sys
sys.setrecursionlimit(10**3)

T = int(input())

def dfs(step, S, L, visited):
    if S == "":
        return True

    for i, s in enumerate(step):
        j = L - len(S) + s - 1
        if visited[j]:
            continue

        visited[j] = True
        if S[s-1] == "0":
            if dfs(step[:i] + step[i+1:], S[s:], L, visited):
                return True
        else:
            continue
    return False

ans = []
for _ in range(T):
    N = int(input())
    S = input().strip()

    ans.append("Yes" if dfs([1 << i for i in range(N)], S, len(S), [False] * len(S)) else "No")

print(*ans, sep="\n")
