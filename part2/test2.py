def solve(n):
    if n%4==0 and n%100!=0 or n%400==0:
        return 1
    else:
        return 0


N=int(input())
print(solve(N))

#boj 2753 윤년