N, K = map(int, input().split())
if N < 2*K - 1:
    print(-1)
else:
    A = [a for a in range(K, K+N, 2)]
    A += [a for a in range(K+1, K+N, 2)]
    B = [b for b in range(K+2*N-N//2-1, K+N-1, -1)]
    B += [b for b in range(K+2*N-1, K+2*N-N//2-1, -1)]
    C = [c for c in range(K+2*N, K+3*N)]
    [print(*p) for p in list(map(list, zip(A, B, C)))]
