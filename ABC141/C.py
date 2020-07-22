N, K, Q = map(int, input().split())
V = [0] * N
for _ in range(Q):
    a = int(input())
    V[a-1] += 1

for v in V:
    print('Yes' if Q-v<K else 'No')
