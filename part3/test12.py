N=int(input())
strs=[input().strip() for _ in range(N)]
strs.sort(key=lambda x:(len(x),[-ord(c) for c in x]))
print(*strs, sep='\n')
#간단한 문자열 정렬문제
