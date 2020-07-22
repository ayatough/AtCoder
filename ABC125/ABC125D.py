# input
n = int(input())
as_ = tuple(int(i) for i in input().split())

# whether the number of negative number is even/odd
# First, calc absolute sum of all element
maxb = sum(abs(a) for a in as_)

# when even negative number
if [a < 0 for a in as_].count(True) % 2 == 0:
    # all element can be positive
    pass
else:
    # all element can be positive, except one element
    smallest = min(abs(a) for a in as_)
    maxb -= smallest * 2

print(maxb)
