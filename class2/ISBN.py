#boj 14626번 ISBN

import sys
input=sys.stdin.readline

num=input().strip()
total=0
target=-1

for i in range(13):
    if num[i]=='*':
        target = i
        continue
    weight =1 if i%2==0 else 3
    total+=int(num[i])*weight

weight=1 if target %2 ==0 else 3
for i in range(10):
    if (total+i*weight)%10==0:
        print(i)
        break
#ㅅㅂ 피곤해서 주석은 달지 않겠슴 대충 보면 어떤식인지 알수 있음.