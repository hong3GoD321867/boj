#boj 11866 요세푸스 문제0
from collections import deque

dq=deque()
yoshep=[]
N,K=map(int,input().split())
for i in range(1,N+1):
    dq.append(i)

for _ in range(N):
    dq.rotate(-(K-1))
    yoshep.append(dq.popleft())


print(f"<{', '.join(map(str,yoshep))}>")

