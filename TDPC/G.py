from bisect import bisect_left
S = input()
K = int(input())
L = len(S)

V = [[] for _ in range(26)]
for i, s in enumerate(S):
    V[ord(s) - ord('a')].append(i)

# dp = [{a: 0 for a in map(chr, range(ord('a'), ord('z')+1))} for _ in range(L+1)]
dp = [[0 for _ in range(26)] for _ in range(L+1)]
dp[1][ord(S[-1]) - ord('a')] = 1

cum = 0
for i in range(2,L+1):
    s = ord(S[-i]) - ord('a')
    dp[i][s] = 1
    # for abc in map(chr, range(ord('a'), ord('z')+1)):
    for abc in range(26):
        dp[i][abc] += dp[i-1][abc]
        # if dp[i-1].get(abc):
        if dp[i-1][abc]:
            dp[i][s] += dp[i-1][abc]
    dp[i][s] -= dp[i-1][s]
    cum += dp[i][s] - 1

ans = []
if cum >= K:
    cnt = K
    pos = 0
    while cnt > 0 and pos < L:
        # for abc in map(chr, range(ord('a'), ord('z')+1)):
        for abc in range(26):
            if cnt - dp[-pos-1][abc] > 0:
                cnt -= dp[-pos-1][abc]
            else:
                ans.append(chr(abc + ord('a')))
                # pos = S.find(ans[-1], pos) + 1
                pos = V[abc][bisect_left(V[abc], pos)] + 1
                cnt -= 1
                break

print(''.join(ans) or 'Eel')
