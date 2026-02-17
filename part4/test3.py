#boj 1914  하노이 탑
def hanoi(n,src,via,dst):
    if n==1:
        print(src,dst)
    else:
        hanoi(n-1,src,dst,via)
        hanoi(1,src,via,dst)
        hanoi(n-1,via,src,dst)
