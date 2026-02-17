num=list(map(int,input().split()))
plus=0
for i in range(len(num)):
    plus+=num[i]*num[i]
print(plus%10)
#boj 2475번 행렬곱셈