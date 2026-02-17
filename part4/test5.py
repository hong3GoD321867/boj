#boj 2448 별 찍기 11
import sys
sys.setrecursionlimit(10**6)

def sierpinski(n,T,row,col):
    if n==3:
        T[row][col]=1
        T[row+1][col-1]=T[row+1][col+1]=1
        for i in range(-2,3):
            T[row+2][col+i]=1
    else:
        m=n//2
        sierpinski(m,T,row,col)
        sierpinski(m,T,row+m,col-m)
        sierpinski(m,T,row+m,col+m)
        #재귀를 이용해서 만들어낸 삼각형 아래 꼭짓점을 기점으로 또다른 삼각형을 만든다.

def solve(n):
    T=[[0]*(2*n-1) for _ in range(n)]
    sierpinski(n,T,0,n-1)
    s=""
    for i in range(n):
        for j in range(2*n-1):
            s+="*" if T[i][j]==1 else " "
        s+="\n"
    print(s)
        
N=int(input())
solve(N)