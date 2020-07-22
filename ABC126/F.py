M, K = map(int, input().split())
MAX_A = 2 ** M

# never exist condition
if 2 ** M <= K or K == 1 and M == 1:
    print(-1)
elif K == 0:
    ary = [i//2 for i in range(MAX_A*2)]
    print(' '.join(map(str, ary)))
else:
    # solution by wrap K
    ary = []
    
    ary_asc = [i for i in range(MAX_A) if i != K]
    ary_dec = [i for i in range(MAX_A-1,-1,-1) if i != K]
    ary.extend(ary_dec)
    ary.extend([K])
    ary.extend(ary_asc)
    ary.extend([K])

    print(' '.join(map(str, ary)))

