S = input()

white = [i for (i, s) in enumerate(S) if s == 'W']
ideal = [i for i in range(len(white))]

print(sum(w - i for (w, i) in zip(white, ideal)))
