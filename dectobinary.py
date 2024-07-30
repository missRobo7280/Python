def decbin(n):
    s=''
    while n>0:
        r=n%2
        s+=str(r)
        n//=2
    return s[ : :-1]#first space is for default starting point and the second dapce is for the default ending point
n=int(input())
print(decbin(n))
