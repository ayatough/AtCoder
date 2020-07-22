H, W, A, B = map(int, input().split())
ans = [[1] * A + [0] * (W-A)] * (H-B) + [[0] * A + [1] * (W-A)] * B
print('\n'.join(''.join(str(e) for e in r) for r in ans))
