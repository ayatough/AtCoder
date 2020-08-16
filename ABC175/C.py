X, K, D = map(int, input().split())
X = abs(X)

def solve():
    if X // D >= K:
        return X - D*K
    if ((X//D)%2 == 0) ^ (K%2 == 0):
        return D - (X - D*(X//D))
    else:
        return X - D*(X//D)

if __name__ == "__main__":
    print(solve())
