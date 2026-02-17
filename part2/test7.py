def is_leap(y):
    return y%4==0 and (y%100!=0 or y%400==0)

def get_days(y,m,d):
    total_days=0
    for i in range(1,y):
        total_days+=366 if is_leap(i) else 365

    month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(1,m):
        total_days+=month_days[i]
        if i==2 and is_leap(y):
            total_days+=1
    return total_days+d

Y1,M1,D1=map(int,input().split())
Y2,M2,D2=map(int,input().split())

if Y2-Y1>1000 or (Y2-Y1==1000 and (M2>M1 or (M2==M1 and D2>=D1))):
    print("gg")
else:
    d_day=get_days(Y2,M2,D2) - get_days(Y1,M1,D1)
    print(f"D-{d_day}")


#boj 1308번 D-Day