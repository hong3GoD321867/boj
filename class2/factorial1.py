 #boj 1676번 팩토리얼 0의 개수

import sys

n=int(sys.stdin.readline())
count=0
while n>=5:
    count+=n//5
    n//=5
print(count)


    

