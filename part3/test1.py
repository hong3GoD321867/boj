#boj 2750 수 정렬하기

#방법1
N=int(input())
nums=[]
for _ in range(N):
    nums.append(int(input()))
nums.sort()
for i in range(N):
    print(nums[i])

#방법2
N=int(input())
nums=[int(input()) for _ in range(N)]
S=sorted(nums)
for i in range(N):
    print(nums[i])

#방법3
N=int(input())
nums=[0]*N
for i in range(N):
    nums[i]=int(input())
nums.sort()
for i in range(N):
    print(nums[i])
