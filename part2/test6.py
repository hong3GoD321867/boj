def solve(n):
    m,cnt=n,1
    while True:
        s=sum(map(int,list(str(m))))
        m=(m%10)*10+(s%10)
        if m==n:
            break
        cnt+=1
    return cnt

N=int(input())
print(solve(N))
#boj 1110 더하기 사이클 ^^7