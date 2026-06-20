N, T, A = map(int, input().split())

print("Yes" if min(T, A) + N - (T + A) < max(T, A) else "No")
