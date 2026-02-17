#boj 1181 단어정렬
import sys
input=sys.stdin.readline

N=int(input())
A=[input().strip() for _ in range(N)] #양쪽 문자열 공백을 제거해줌
A=list(set(A)) #A를 집합으로 바꿔서 변화없는상태에서 리스트로 전환
A.sort(key=lambda x:(len(x),x))
print("\n".join(A))
