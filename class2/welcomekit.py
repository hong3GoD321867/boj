#boj 30802번 웰컴 키트

#티셔츠랑 볼펜 하나 받는디. 근데 티셔츠가 사이즈가 총 6개여.
#티셔츠는  T장 묶음으로 , 볼펜을 P장 묶음으로 주문 가능하다. 
import sys
input=sys.stdin.readline

N=int(input())
S=list(map(int,input().split()))
T,P=map(int,input().split())

total_t_bundles =0
for size_count in S:
    if size_count ==0:
        continue
    total_t_bundles+=(size_count-1)//T+1 #이래해야 소수점이여도 반올림이 된다네요.

print(total_t_bundles)
print(N//P,N%P)






#같은 사이즈의 T장 묶음으로 주문가능, S를 6개 묶음으로 주문한다.
#펜은 P장 묶음으로 주문 가능, or 한자루씩 주문가능 펜 6개 묶음으로 주문하고 2개 더 주문이런식으로가능

#같은 5개씩 




