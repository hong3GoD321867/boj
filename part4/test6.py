#boj 2057 팩토리얼 분해
# 아이디어 greedy: 가장 큰 팩토리얼 부터 빼내자!
import sys

def solve():
    N=int(sys.stdin.readline())

    if N==0:
        print("NO")
        return 
    # 0!부터 20!까지의 팩토리얼의 값을 리스트에 넣어두기
    fact=[1]*21
    for i in range(1,21):
        fact[i]=fact[i-1]*i
    
    # 큰 값부터 빼주는 그리디 알고리즘 적용
    for i in range(20,-1,-1):
        if N>=fact[i]:
            N-=fact[i]
    #원래 N에서 fact을 하나씩 빼다가 N이 0이되면 끝! 팩토리얼의 합으로 표현이 가능한거임.
    if N==0:
        print("YES")
    else:
        print("NO")

solve()

