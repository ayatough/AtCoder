m = int(input())

if m < 100:
    vv ='00'
elif m < 5000:
    vv = ('0' + str(int(m / 1000 * 10)))[-2:]
elif m < 30000:
    vv = int(m / 1000 + 50)
elif m < 70000:
    vv = int((m / 1000 - 30) / 5 + 80)
else:
    vv = 89

print(vv)