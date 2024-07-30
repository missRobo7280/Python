'''a=list(map(int,input().split()))
b=int(input())
print(a.count(b))'''

a=list(map(int,input().split()))
b=int(input())
d=b
c=0
for i in range(len(a)):
    if a[i]==d:
        c+=1

print(c)
