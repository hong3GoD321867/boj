N=int(input())
nums= [int(input()) for _ in range(N)]
nums.sort(reverse=True)
for i in range(N):
    print(nums[i])

#내림차순 정렬할때 사용하는거
