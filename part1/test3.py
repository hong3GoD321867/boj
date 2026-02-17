def solve(N,M):
    s=0
    for i in range(N,M+1):
        s+=i
    return s

N=int(input())
M=int(input())
print(solve(N,M))