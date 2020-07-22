S = input()
K = int(input())
for i, s in enumerate(S):
    if s != '1':
        break
if K <= i:
    print(1)
else:
    print(s)
