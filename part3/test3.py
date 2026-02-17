#boj 2751 수 정렬하기 2
import sys
input=sys.stdin.readline

N=int(input())
nums=[int(input()) for _ in range(N)]
nums.sort()
for i in range(N):
    print(nums[i])
