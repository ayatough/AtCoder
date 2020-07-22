# input
A, B, C = map(int, input().split())

poi = min(A+B+1, C)
print(poi + B)
