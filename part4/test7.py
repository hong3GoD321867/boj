# boj 16953 A->B
#정수 A를 B로 바꿔야함 할수있는건 2를 곱하거나, 1을 일의자리수의 추가해주는것뿐.
import sys
input=sys.stdin.readline
a,b=map(int,input().split())
result=1

while b!=a:
    result+=1

    tmp=b

    if b%10==1:
        b//=10
    elif b%2==0:
        b//=2
    
    if tmp==b:
        print(-1)
        break
    
else:
    print(result)