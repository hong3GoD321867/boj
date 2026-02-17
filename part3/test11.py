nums=list(map(int,input().split()))
nums.sort(key=lambda x:(len(str(x)),-x))
print(*nums)
#자릿수 끼리는 오름차순, 같은 자릿수에서는 내림차순
