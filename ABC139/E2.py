def main():
    import sys

    input = sys.stdin.readline
    N = int(input())
    A = []

    def intm1(a):
        return int(a) - 1

    A = [list(map(intm1, input().split())) for _ in range(N)]

    B = [0] * N

    nokori = N*(N-1)
    day = 0

    for _ in range(N*(N-1)//2):
        day += 1
        ng = [False] * N
        upd = False
        for i in range(N):
            if ng[i] or B[i] == N-1:
                continue
            j = A[i][B[i]]
            if not ng[j] and B[j] < N-1 and A[j][B[j]] == i:
                ng[A[i][B[i]]] = True
                ng[A[j][B[j]]] = True
                B[i] += 1
                B[j] += 1
                upd = True
                nokori -= 2
        if not upd or nokori == 0:
            break

    print(day if nokori == 0 else -1)

if __name__ == "__main__":
    main()