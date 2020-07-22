S = input()
easy = True
for i, s in enumerate(S):
    if i%2 == 0 and s == 'L':
        easy = False
        break
    if i%2 == 1 and s == 'R':
        easy = False
        break
print('Yes' if easy else 'No')
