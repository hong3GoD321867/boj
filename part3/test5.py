#만약 x좌표는 오름차순으로 정렬, y좌표를 내림차순으로 정렬하면?

import sys
input=sys.stdin.readline

N=int(input())
nums=[list(map(int,input().split)) for _ in range(N)]
nums.sort(key=lambda x: (x[0],-x[1]))
for i in range(N):
    print(" ".join(map(str,nums[i])))