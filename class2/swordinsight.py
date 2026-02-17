import sys

n_str=sys.stdin.readline().strip()

nums=sorted([int(x) for x in n_str], reverse=True)
plus=0
for i in range(len(nums)):
    plus+=nums[i]*(10**(len(nums)-1-i))

print(plus)

#수학적 풀이-> 소드인사이트는 입력한 숫자의 값을 내림차순으로 정렬하도록 하는 알고리즘.
#boj 1427번 소드인사이드