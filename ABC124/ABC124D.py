# input
n, k = (int(i) for i in input().split())
s = input()


# first, end: '1'
def make_chain(l):
    chn = []
    prev = '1'
    chn.append(0)
    for elem in l:
        if elem != prev:
            chn.append(1)
        else:
            chn[-1] += 1
        prev = elem
    if not l[-1] == '1':
        chn.append(0)
    return chn

chn = make_chain(s)

chn_sums = []
sum_len = 2 * k + 1
chn_sum = sum(chn[:sum_len])
chn_sums.append(chn_sum)
for i in range(0, len(chn) - sum_len, 2):
    # drop prev 1st and 2nd, append next 1st ad 2nd
    chn_sum = chn_sum - chn[i] - chn[i+1] + chn[i+sum_len] + chn[i+sum_len+1]
    chn_sums.append(chn_sum)


print(max(chn_sums))
