#fibonacci number before entered number using recursion
def fib(n):
    a,b=0,1
    
    i=2
    while True:
        c=a+b
        a=b
        b=c
        if b>n:
            print(a)
            break
        i+=1    
n=int(input())
fib(n)
    
