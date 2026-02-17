import sys
input=sys.stdin.readline
N=int(input())
num=[]
for _ in range(N):
    val=int(input())
    num.append(val)
num.sort()
for i in range(N):
    print(num[i])

#boj 15688번 수 정렬하기 5