##n=int(input())
##l=list(map(int,input().split()))
##c=0
##for i in range(1,n+1):
##    if l[i+1]%2==0:
##        if l[i-1]%2==0 and l[i+1]%2==0:
##            c+=1            
##print(c)
##
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    if l[i]%2==0:
        for i  in l:
            if i%2==1:
                c+=1
if(c>0):
    print("False")
else:
    print("True")
        

