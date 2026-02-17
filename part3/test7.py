#boj 10818 최소/최대
N=int(input())
nums=map(int,input().split())
nums.sort()
print(nums[0],nums[-1])

#다른 풀이

def solve(n,A):
    smallest,largest=10**6,-10**6
    for i in range(n):
        smallest=min(smallest,A[i])
        largest=max(largest,A[i])
    return smallest,largest

N=int(input())
A=list(map(int,input().split()))
s,l=solve(N,A)
print(s,l)
#함수 만들고, max,min 써서 푸는 방식 요건 살짝 c느낌임.