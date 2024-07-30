'''a=list(map(int,input().split()))
b=int(input())
for i in range(len(a)):
    if a[i]==b:
        print(i,end=' ')'''

a=list(map(int,input().split()))
b=int(input())
for i in range(len(a)):
    if a[i]==b:
        print(a.index(b),end=' ')
        a[i]=-1#we changed the list
