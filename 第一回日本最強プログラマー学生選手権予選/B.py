N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

H = [[b < a for b in A[:i]].count(True) for i, a in enumerate(A)]  # hukkisuu
T = [[b < a for b in A[i+1:]].count(True) for i, a in enumerate(A)]  # tentousuu

print(sum(h*K*(K-1)//2 + t*K*(K+1)//2 for h, t in zip(H, T)) % MOD)
