N, K = map(int, input().split())
S = input()

happy = 0
for i in range(1,N):
    if S[i] == S[i-1]:
        happy += 1

turn = N - happy - 1

for i in range(K):
    if turn <= 0:
        break
    elif turn == 1:
        happy += 1
        turn -= 1
    else:
        happy += 2
        turn -= 2

print(happy)
