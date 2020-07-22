S = input()
T = input()
SD = dict()
TD = dict()

valid = True
for s, t in zip(S, T):
    if s not in SD.keys():
        SD[s] = t
    else:
        if SD[s] != t:
            valid = False
            break
    if t not in TD.keys():
        TD[t] = s
    else:
        if TD[t] != s:
            valid = False
            break

print('Yes' if valid else 'No') 
