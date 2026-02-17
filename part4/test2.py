#boj 4564번 숫자 카드놀이
import sys
sys.setrecursionlimit(10**5)

def solve(n):
    print(n,end=" ")
    s=str(n)
    if len(s)>1:
        prod=1
        for i in range(len(s)):
            prod*=int(s[i])
        solve(prod)
    else:
        print()

while True:
    N=int(input())
    if N==0:
        break
    solve(N)

