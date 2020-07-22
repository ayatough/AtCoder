# input
n = int(input())
# edges = set()
# for _ in range(n-1):
#     edges.add(tuple(int(i) for i in input().split()))

edges = set(tuple(int(i) for i in input().split()) for _ in range(n-1))
pass
