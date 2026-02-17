N=int(input())
nums=[list(map(int,input().split())) for _ in range(N)]
nums.sort(key=lambda x:(x[1],x[0]))
for i in range(len(nums)):
    print(*nums[i])
#boj 10814번 나이순정렬