# input
x, y, z, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

ab = []
ab.extend([i+j for j in b[:k] for i in a[:k]])
ab.sort(reverse=True)

abc = []
abc.extend([i+j for j in ab[:k] for i in c[:k]])
abc.sort(reverse=True)

print('\n'.join(str(i) for i in abc[:k]))
