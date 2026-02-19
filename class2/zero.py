#boj 10773번 zero
#queue 사용
from collections import deque

N=int(input())
dq=deque()
for _ in range(N):
    dq.appendleft(int(input()))
    if dq[0] == 0:
        dq.popleft()
        dq.popleft()
print(sum(dq))


    
