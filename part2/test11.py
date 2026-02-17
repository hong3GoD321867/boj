import math
num1=int(input())
num2=int(input())
dist=[]
sum=0
for m in range(num1,num2+1):
    if m%math.sqrt(m)==0: #제곱근은 math 라이브러리를 이용하여 만든다.
        dist.append(m)
        sum+=m
        

if not dist:
    print(-1)
else:
    print(sum)
    print(min(dist))       
#boj 1977 완전제곱수