N = int(input())
P = list(map(int, input().split()))

I = [0] * N
for i in range(N):
    I[P[i]-1] = i

ans = 0
'''
L[i]: Pにおいてi番目の位置にあるp(0~N)において、そこから左を順に見て行って、pより真に大きい値が初めて出てくる場所、Rも同様
無い場合は左に見ていく場合は-1、右に見ていく場合はN
pを1からNまでなめることで随時更新する
L,Rの更新後で整合性が保たれていることとなる
'''
L = [i for i in range(-1, N-1)]
R = [i for i in range(1, N+1)]
'''
初期値はp=0のときと考えられる（両隣は真に大きい）
'''
for p in range(1,N+1): # 1からN-1までで十分だが、L,Rの最終状態を確認するためNまで回す
    i = I[p-1]
    # L, R の更新、ここの意味は具体的に例を考えないと理解できなかった...
    if R[i] < N:
        L[R[i]] = L[i]
    if L[i] >= 0:
        R[L[i]] = R[i]

    l1 = L[i]
    l2 = L[l1] if l1 >= 0 else -1  # l1の場所から考えることでOK、l1がすでに端に到達している場合に注意
    r1 = R[i]
    r2 = R[r1] if r1 < N else N
    ans += p * ((r1-i)*(l1-l2) + (i-l1)*(r2-r1))

print(ans)
