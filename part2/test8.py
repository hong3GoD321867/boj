def solve(H,M,p):
    if M+p<60:
        return H,M+p
    else:
        H=(H+(M+p)//60)%24
        M=(M+p)%60
    return H,M



H,M=map(int,input().split())
plus=int(input())

H,M=solve(H,M,plus)
print(H,M)
#boj 2525번 오븐시계