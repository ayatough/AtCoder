import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = input().strip()

def smallest_subsequence(s: str, k: int) -> str:
    n = len(s)
    stack = []
    for i in range(n):
        while stack and stack[-1] > s[i] and len(stack) + n - i > k:
            stack.pop()
        if len(stack) < k:
            stack.append(s[i])
    return ''.join(stack)

print(smallest_subsequence(S, K))
# anser by ChatGPT
