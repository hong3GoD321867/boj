#boj 2164번 카드2
#queue 개념 사용--> deque 라이브러리 사용

from collections import deque
N=int(input())
deque =deque([i for i in range(1,N+1)])

while len(deque)>1:
    #왼쪽거를 빼내고 오른쪽에 넣는다
    deque.popleft()
    move_num=deque.popleft()
    deque.append(move_num)

print(deque[0])