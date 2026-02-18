#boj 2798번 블랙잭

import sys
input=sys.stdin.readline

N,M=map(int,input().split())
a=list(map(int,input().split()))
b=[]
#이 알고리즘 상당히 마싰다.
for i in range(len(a)-2):
    for j in range(i+1,len(a)-1):
        for k in range(j+1,len(a)):
            if M-(a[i]+a[j]+a[k])>=0:
                b.append(a[i]+a[j]+a[k])
#브루트 포스 문제 깔끔한 반복문 사용으로 양 사이드로 한 칸 간격으로 비교하면서 전체를 비교한다.
print(max(b))
