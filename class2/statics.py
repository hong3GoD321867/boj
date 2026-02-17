from collections import Counter
import sys

input=sys.stdin.readline

N=int(input())
stic=[]
sum=0
for i in range(N):
    val=int(input())
    stic.append(val)
    sum+=val
stic.sort()
#산술 평균
print(int(round(sum/N))) #round에서 오차가 발생할수도 있기 때문에 이부분유의해서 int로 확실하게
#중앙값
print(stic[N//2])
#최빈값, ->Counter는 최빈값을 찾아주는 라이브러리이고 counts.most_common은 최빈값의 데이터를 저장해주는 리스트이다.
counts=Counter(stic)
modes=counts.most_common()
modes.sort(key=lambda x:(-x[1],x[0]))
if len(modes)>1 and modes[0][1]==modes[1][1]:
    print(modes[1][0])
else:
    print(modes[0][0])
#범위
print(stic[-1]-stic[0])
    
#boj 2108 통계학