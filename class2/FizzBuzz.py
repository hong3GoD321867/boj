#boj 28702번 Fizzbuzz

for i in range(3,0,-1):
    x=input()
    if x not in ['Fizz','Buzz','FizzBuzz']:
        n=int(x)+i
#요기 까지가 되게 참신한 생각인거같음...
if n%3==0 and n%5==0:
    print('FizzBuzz')
elif n%3==0:
    print('Fizz')
elif n%5==0:
    print('Buzz')
else:
    print(n)