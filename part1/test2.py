def change_maker(W,units):
    count=[0]*len(units)
    for i in range(len(units)):
        count[i]=W//units[i]
        W=W%units[i]
    return count


units=[50000,10000,5000,1000,500,100,50,10,5,1]
W=26240
result=change_maker(W,units)
for u,c in zip(units,result):
    print(f"{u}원: {c}개")