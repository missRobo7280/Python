#collatz sequence
n=int(input())
if n%2==0:

    i=1
    t=n
    while n>1:
        print(t)
        t=t//2
else:
    i=1
    t=n
    while n!=1:
        print(t)
        t=(3*t+1)
    


 def collatz(n):
        while n>1:
            if n%2==0:
                n//=2
        else:
            n=3*n+1
        print(n)
    n=int(input())
    collatz(n)
           
