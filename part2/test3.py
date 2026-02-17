def solve(h,m):
    if m>=45:
        m=m-45
    else:
        m=(m-45)%60
        h=(h-1)%24
    return h,m

h,m=map(int,input().split())
h,m=solve(h,m)
print(h,m)

#boj 2884 알람시계
