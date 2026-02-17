import sys
input=sys.stdin.readline

N=int(input())
login=[list(map(str,input().split())) for _ in range(N)]
login.sort(key=lambda x:(int(x[0])))
for i in range(len(login)):
    print(*login[i])

#야호 나이순으로 가는코드임. 나이는 오름차순 나이가 같으면 가입순
#boj 10814 나이순정렬