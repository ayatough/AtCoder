N, K = map(int, input().split())
S = list(input())

def swap(T, i, j):
    _ = T[i]
    T[i] = T[j]
    T[j] = _
    
k = 0
memo = set()
T = S.copy()
for i in range(N):
    for m in sorted(T[i:]):
        j = i + T[i:].index(m)
        if i == j:
            break
        cnt = 0
        cnt += 0 if i in memo else 1
        cnt += 0 if j in memo else 1
        cnt -= 1 if S[i] == m else 0
        if k + cnt <= K:
            swap(T, i, j)
            k += cnt
            memo.add(i)
            memo.add(j)
            break

print(''.join(T))
