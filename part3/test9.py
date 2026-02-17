#boj 5618 공약수

def solve(n,A):
    m=min(A)
    for k in range(1,m+1):
        if A[0]%k==0 and A[1]%k==0:
            if n==2:
                print(k)
            elif n==3 and A[2]%k==0:
                print(k)
N=int(input())
A=list(map(int,input().split()))
solve(N,A)
