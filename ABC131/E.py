from itertools import combinations
N, K = map(int, input().split())

def solve():
    uni = []  # max is uni !!!
    for i in range(N-1):
        v = i + 2
        uni.append((1, v))
    f = (N - 1) * (N - 2) // 2

    for edge in combinations(range(2, N+1), 2):
        if f == K:
            break
        uni.append(edge)
        f -= 1
    
    return len(uni), uni
    

if K > (N - 1) * (N - 2) // 2:
    print(-1)
else:
    M, G = solve()
    print(M)
    for g in G:
        print(g[0], g[1])