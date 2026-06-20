"""calculate #{p<=N: p is prime number} by Lucy DP
"""

N = int(input())

# S(i,n) := #{p: 2<=p<=n, remained with Sieve of Eratosthenes every q which is lower than i}
# S(i,n) = S(i-1,n) - S(i-1,n//i) + S(i-1,i-1) if i is prime number and i*i<=n
# S(i,n) = S(i-1,n)                            otherwise
# #{p<=N: p is prime number} = S(n,n)

NS = int(N**0.5)
V = [N//i for i in range(1,NS+1)]
V += [i for i in range(V[-1]-1,0,-1)]

# calc S(1,n)
S = {i: i-1 for i in V}

# print(f"{S=}")

for i in range(2,NS+1):
    # S(i,i) = S(i,i-1) => i is not prime
    if S[i] == S[i-1]:
        continue

    for n in V:
        if i*i > n:
            break
        S[n] += -S[n//i] + S[i-1]

    # print(f"{i=}, {S=}")

print(S[N])

# S2(i,n) := sum(p)_{2<=p<=n, remained with Sieve of Eratosthenes every q which is lower than i}
# S2(i,n) = S2(i-1,n) - i*(S2(i-1,n//i) - S2(i-1,i-1)) if i is prime number and i*i<=n
# S2(i,n) = S2(i-1,n)                              otherwise
# sum(p)_{p<=N: p is prime number} = S2(n,n)

# calc S2(1,n)
S2 = {i: (i+2)*(i-1)//2 for i in V}

# print(f"{S2=}")

for i in range(2,NS+1):
    # S2(i,i) = S2(i,i-1) => i is not prime
    if S2[i] == S2[i-1]:
        continue

    for n in V:
        if i*i > n:
            break
        S2[n] += -i*(S2[n//i] - S2[i-1])

    # print(f"{i=}, {S2=}")

print(S2[N])
