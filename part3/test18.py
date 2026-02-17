import sys
input=sys.stdin.readline

N=int(input())
arr=[]
for i in range(N):
    val=int(input())
    arr.append(val)
arr.sort(reverse=True)
for i in range(N):
    print(arr[i])
#boj 11931 수 정렬하기4