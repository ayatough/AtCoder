N = int(input())
W = list(map(int, input().split()))
print(min(abs(sum(W[:i]) - sum(W[i:])) for (i, w) in enumerate(W)))
