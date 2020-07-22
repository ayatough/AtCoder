# input
n = int(input())
s = input()


prod = 1
for char in set(s):
    num = s.count(char)
    prod *= (num + 1)

print((prod - 1) % (pow(10, 9) + 7))

# my challange code

# from itertools import combinations

# # input
# n = int(input())
# s = input()


# # s frequent list
# def make_freq(s):
#     freq_s = []
#     uniq_s = set(s)
#     for char in uniq_s:
#         freq_s.append(s.count(char))

#     freq_s.sort(reverse=True)
#     return freq_s

# freq_s = make_freq(s)


# # tuple product calc
# def product(t):
#     if len(t) == 0:
#         return 0
#     prod = 1
#     for i in t:
#         prod *= i
#     return prod


# # clac product i conbination
# print(sum(product(comb) for i in range(len(freq_s)) for comb in combinations(freq_s, i + 1)))
