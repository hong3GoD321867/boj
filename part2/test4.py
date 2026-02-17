def solve(n):
    for m in range(1,n+1):
        if n==m+sum(map(int,str(m))):
            return m
        
N=int(input())
print(solve(N))
#boj 2738 분해합