#boj 1931번 회의실 배정
import sys
input=sys.stdin.readline

N=int(input())
endPoint=0
answer=0

arr=[]
for i in range(0,N):
    a,b=map(int,input().split())
    arr.append([a,b])

arr.sort(key=lambda x:(x[1],x[0]))

for newStart,newEnd in arr:
    if endPoint<=newStart:
        answer+=1
        endPoint=newEnd
print(answer)


