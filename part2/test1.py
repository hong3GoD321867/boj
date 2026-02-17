#자료형 정리

#int,float,bool,str,list,tuple,set,dict
#파이썬은 dynamic typing->즉 변수를 쓸때 자료형을 정하는 형식이다.

#if문 사용법
x=7
if x%2==0:
    print("even")
elif x%3==0:
    print("div by 3")
else:
    print("odd")
#반복문
arr=[3,5,7,9]
for i in range(len(arr)):
    arr[i]*=2
print(arr)

s="ABC"
for ch in s: #문자열을 문자하나씩 출력
    print(ch,end=" ")

nums=[10,20,30]
for x in nums:
    print(x)

scores={"kim":95,"lee":88}
for k in scores:
    print(k,scores[k])

#함수선언
def add(a,b):
    return a+b

x=add(2,3)

#리스트 활용문법

squares=[]
for x in range(10):
    squares.append(x**2)
print(squares)

squares=list(map(lambda x: x**2,range(10)))
print(squares)

#리스트 컴프리헨션
M1=[(i,j) for j in range(3) for i in range(2)]
print(M1)

M2=[[(i,j) for j in range(3)] for i in range(2)]
print(M2)

a=[i for i in range(1,11)]
b=[j for j in a if a[-1]%j==0] #1,2,5,10

#표준입력 split()-> 한줄에 여러개의 입력이 있을때 공백으로 구분하여 토큰화한다.
#표준입력 map()-> 각 토큰화되어 있는 값의 자료형을 변환시켜준다.

s=input()
print(s)

n=int(input())
print(n)

s,t=input().split()
print(s,t)

a,b=map(int,input().split())
print(a,b)

nums=list(map(int,input().split()))
print(nums)

n=int(input())
nums=[int(input()) for _ in range(n)]
print(nums)

