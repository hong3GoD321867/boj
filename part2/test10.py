def solve(a,b,n,k1,m):
    X=[[0]*k1 for _ in range(n)]
    for i in range(n):
        for j in range(k1):
            for k in range(m):
                X[i][j]+=a[i][k]*b[k][j] #행렬 곱셈 알고리즘.

    return X
N,M=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(N)]
M,K=map(int,input().split())
B=[list(map(int,input().split())) for _ in range(M)]

mul=solve(A,B,N,K,M)

for row in mul:
    print(*row)
#이런식으로 mul리스트안에 있는 것을 *row을 이용하여 리스트 전체를 보여줄수 있다.

#boj 2740번 행렬곱셈
            

