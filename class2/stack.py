#boj 1874번 스택 수열

import sys
input=sys.stdin.readline

n=int(input())
st=[]
op=[]
cur=1

for _ in range(n):
    num =int(input())

    while cur <=num:
        st.append(cur)
        op.append('+')
        cur+=1

    if st[-1]==num:
        st.pop()
        op.append('-')
    else:
        print('NO')
        break
if not st:
    print("\n".join(op))