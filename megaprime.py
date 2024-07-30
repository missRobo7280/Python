n=int(input())
for i in range(2,int(n**0.5)+1):
    if n%i==0:
        print(False)
        break
else:
    print(True)
    
for i in range(1,n+1):
    rev=0
    t=n
    while t!=0:
        r=n%10
        t=t//10

a=r
for i in range(2,int(r**0.5)+1):
    if a%i==0:
        print(False)
        break
else:
    print(True)

b=t
for i in range(2,int(b**0.5)+1):
    if b%i==0:
        print(False)
        break
else:
    print(True)

        
