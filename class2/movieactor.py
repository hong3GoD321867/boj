#boj 1436번 영화감독 숌

#완전 탐색 ->브루트 포스 알고리즘 사용: 가능한 모든 수의 조합을 다 찾는 방식

N=int(input())
cnt=0
result =666
#코드를 보면 단순하지만 사실 어마무시함.. 엄청나게 반복을 많이 할 가능성이 있는 알고리즘인듯.
while True:
    if '666' in str(result):
        cnt+=1
    if cnt==N:
        break
    result+=1

print(result)