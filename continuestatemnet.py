a,b,c=map(int,input().split())
i=1
if a>b:
    a,b=b,a
while b>a:
    if a==c:
        print(True)
        break
    a+=1
        
else:
    print(False)
    

        
        
    
