_ = int(input())

ans = []

A = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
a =  ord("a")

for s in input().split(" "):
    ans.append(str(A[ord(s[0]) - a]))

print("".join(ans))
