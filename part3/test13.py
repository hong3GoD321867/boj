#하샤드 수
def solve(nums):
    indices=[]
    for i,num in enumerate(nums):
        s=sum(num//10,num%10)
        if num%s==0:
            indices.append(i)
    return indices if indices else [-1]

nums=list(map(int,input().split()))
result=solve(nums)
print(*result)

