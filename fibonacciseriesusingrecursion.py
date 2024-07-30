#fibonacci series using recursion
def fib(n):
    a,b=0,1#we can declare two variables together in sequence
    print(a,b,end=' ')
    for i in range(2,n):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
n=int(input())
fib(n)
    
