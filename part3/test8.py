#boj 2501 약수구하기
def solve(n,k):
    cnt=0
    for d in range(1,n+1):
        if n%d==0:
            cnt+=1
        if cnt==k:
            return d
    return 0

N,K=map(int,input().split())
print(solve(N,K))

#다른 방법

def divisor(n):
    div=set()
    for d in range(1,int(n**0.5)+1):
        if n%d==0:
            div.add(d)
            div.add(n//d)
    return sorted(list(div))

N,K=map(int,input().split())
D=divisor(N)
print(D[K-1] if K<=len(D) else 0)
