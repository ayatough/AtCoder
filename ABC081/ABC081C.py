n, k = (int(i) for i in input().split())
balls = (int(i) for i in input().split())
freqs = {}
for ball in balls:
    # ball = int(input())
    freqs[ball] = freqs[ball] + 1 if ball in freqs else 1
freq_hist = list(freqs.values())
# ball_set = set(balls)
# freqs = list(balls.count(i) for i in ball_set)
freq_hist.sort(reverse=True)
print(sum(freq_hist[k:]))
