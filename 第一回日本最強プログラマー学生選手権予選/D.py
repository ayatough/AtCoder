''' Keyword
二部グラフ, bipartite graph
'''

N = int(input())
for i in range(N-1):
    level = []
    for j in range(i+1, N):
        for k in range(N.bit_length()):
            if (i ^ j) >> k & 1:
                level += [k+1]
                break
    print(*level)
