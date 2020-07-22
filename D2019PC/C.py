# input
N = int(input())
S = [input() for _ in range(N)]

inner_count = sum(s.count('AB') for s in S)

a_ends = []
b_bgns = []
for i, s in enumerate(S):
    if s[0] == 'B':
        b_bgns.append(i)
    if s[-1] == 'A':
        a_ends.append(i)

match_flag = 0
if set(a_ends) == set(b_bgns):
    match_flag = 1
join_count = max(min(len(a_ends), len(b_bgns)) - match_flag, 0)

print(inner_count + join_count)
