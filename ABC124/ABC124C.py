# input
s = input()
bins = [b == '1' for b in s]

pattern_a = ([True, False] * ((len(s) // 2) + 1))[:len(s)]
pattern_b = ([False, True] * ((len(s) // 2) + 1))[:len(s)]

pat_a_min = [p ^ q for p, q in zip(bins, pattern_a)].count(True)
pat_b_min = [p ^ q for p, q in zip(bins, pattern_b)].count(True)

print(min(pat_a_min, pat_b_min))
