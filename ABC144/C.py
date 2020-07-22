N = int(input())
print(min(i-1 + N//i-1 for i in range(1,int(N**0.5)+1) if N%i == 0))