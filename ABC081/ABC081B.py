n = int(input())
as_ = (int(i) for i in input().split())
pow2s = [len(bin(i)) - bin(i).rfind('1') - 1 for i in as_]
print(min(pow2s))
