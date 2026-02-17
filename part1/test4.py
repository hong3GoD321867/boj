def change_maker(W,units):
    count=[0]*len(units)
    for i in range(len(units)):
        count[i]=W//units[i]
        W=W%units[i]
    return count

W=int(input())
units=[50000,10000,5000,1000,500,100,50,10,5,1]
result=change_maker(W,units)
print(sum(result))
for u,c in zip(units,result):
    if c!=0:
        print(f"{u}: {c}")