#boj 3943 헤일스톤 수열
import sys
input=sys.stdin.readline

def get_hailstone_max(n):
    max_val=n
    current=n
    while current!=1:
        if current%2==0:
            current//=2
        else:
            current=current*3+1

        if current>max_val:
            max_val=current
    return max_val

T=int(input())
for _ in range(T):
    n=int(input())
    print(get_hailstone_max(n))