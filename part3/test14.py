sentence=input()
sentences=list(map(str,input().split()))
num=0

for i in range(len(sentences)):
    if sorted(sentence)==sorted(sentences[i]):
        num+=1
print(num)
#애너그램 같은 수 갯수구하기 코드