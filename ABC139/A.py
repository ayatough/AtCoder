S = input()
T = input()
print([s==t for (s,t) in zip(S,T)].count(True))
