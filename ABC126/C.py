N, K = map(int, input().split())

# neccesary count
def ncount(k):
    count = 0
    cur = k
    while cur < K:
        cur <<= 1
        count += 1
    return count

print(sum(0.5 ** ncount(n) for n in range(1, N+1)) / N)

