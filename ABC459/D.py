from heapq import heapify, heappop, heappush

T = int(input())
N = 26
a = ord("a")

for _ in range(T):
    S = input().strip()
    L = len(S)
    mas = [0] * N
    counter = [0] * (L + 1)
    counter[0] = N
    maxv = 0
    for s in S:
        i = ord(s) - a
        counter[mas[i]] -= 1
        mas[i] += 1
        counter[mas[i]] += 1
        maxv = max(mas[i], maxv)
    # print(mas, counter, maxv)
    if maxv > (L + 1) // 2:
        print("No")
    else:
        print("Yes")
        ranking = [(-mas[i - a], chr(i)) for i in range(a, a + 26) if mas[i - a] > 0]
        ranking.sort()
        # print(ranking)
        heapify(ranking)
        safes = []
        while len(safes) < L:
            top = heappop(ranking)
            if len(safes) > 0 and safes[-1] == top[1]:
                second = heappop(ranking)
                safes.append(second[1])
                heappush(ranking, (second[0] + 1, second[1]))
                heappush(ranking, top)
            else:
                safes.append(top[1])
                heappush(ranking, (top[0] + 1, top[1]))
        print("".join(safes))
