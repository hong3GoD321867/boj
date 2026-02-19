# boj 18110 solved.ac
import sys
from collections import deque
input=sys.stdin.readline

line =input().strip()
if not line:
    exit()

N=int(line)

if N==0:
    print(0)
    exit()
scores=[]
for _ in range(N):
    scores.append(int(input()))
scores.sort()

act=deque(scores)

K=int(N*0.15+0.5)

for _ in range(K):
    act.pop()
    act.popleft()

#결과 계산하때 나머지 인원수로 나누자
remaining_count=len(act)

if remaining_count==0:
    print(0)
else:
    avg=sum(act) / remaining_count
    print(int(avg+0.5))