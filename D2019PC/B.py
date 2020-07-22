# input
R, G, B, N = map(int, input().split())

rmax = N // R

count = 0
for r in range(rmax+1):
    rem = N - r * R
    gmax = rem // G
    for g in range(gmax+1):
        remm = rem - g * G
        if remm % B == 0:
            count += 1

print(count)
