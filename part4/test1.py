#재귀 boj 10872 팩토리얼
import sys
sys.setrecursionlimit(10**5)

def solve(n):
    if n==0:
        return 1
    else:
        return n*solve(n-1)
N=int(input())
print(solve(N))
