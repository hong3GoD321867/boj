#유레카 이론
triangle=[n*(n+1)//2 for n in range(1,46)]
eureka=[0]*1001

for i in triangle:
    for j in triangle:
        for k in triangle:
            if i+j+k<=1000:
                eureka[i+j+k]=1
#미리 값이 천 이하인 모든 삼각비의 수를 구해놓고 경우를 3개의 삼각비로 만들수 있는 값 경우를 다 1로 저장해놓는다,

T=int(input())
for _ in range(T):
    print(eureka[int(input())])