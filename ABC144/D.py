from math import atan2, degrees
A, B, X = map(int, input().split())
if X < A*A*B/2:
    theta = atan2(A*B*B, 2*X)
else:
    theta = atan2(2*(A*A*B-X),A**3)
print(degrees(theta))