#6518번 콜라츠 추측 문제

import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def collatz(n,path):
    path.append(n)
    if n==1:
        return path
    if n%2==0:
        return collatz(n//2,path)
    else:
        return collatz(3*n+1,path)
    
def solve(A,B):
    path_a=collatz(A,[])[::-1] #수열은 반대로 슬라이싱
    path_b=collatz(B,[])[::-1]

    minlen=min(len(path_a),len(path_b))
    i=0
    while i<minlen:
        if path_a[i] != path_b[i]:
            break
        i+=1
    return len(path_a)-i,len(path_b)-i,path_a[i-1]

while True:
    line=input().split()
    if not line: break
    A,B=map(int,line)
    if A==0 and B==0:
        break
    a1,a2,a3=solve(A,B)
    print(f"{A} needs {a1} steps, {B} needs {a2} steps, they meet at {a3}")