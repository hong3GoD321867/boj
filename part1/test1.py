def change_maker(W,units):
    count=[0]*len(units)
    for i in range(len(units)):
        while W>=units[i]:
            W=W-units[i]
            count[i]=count[i]+1
    return count

units=[50000,10000,5000,1000,500,100,50,10,5,1]
W=26240

result=change_maker(W,units)
for u,c in zip(units,result): #zip은 리스트들을 묶어서 튜플형태로 반환시켜주는 역할.
        print(f"{u}원: {c}개")