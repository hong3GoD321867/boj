#boj 11650 좌표 정렬하기
import sys
input=sys.stdin.readline

N=int(input())
nums=[tuple(map(int,input().split())) for _ in range(N)]
nums.sort()
for i in range(len(nums)):
    print(" ".join(map(str,nums[i])))
#tuple은 항상 인덱스랑 원소값이 고정이다! 그래서 x축 y축 이런 2개를 기준으로 하는 그런알고리즘에서 유용하다.
#변화가 없어야한다!