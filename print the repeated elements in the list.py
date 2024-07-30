# program to print the repeated elements in the list
a=list(map(int,input().split()))
'''for i in range(len(a)):
    if a.count(i)>1:
        print(i)'''
b=[]
for i in a:
    if i not in b and a.count(i)>1:#memebership operators in and not in
        b.append(i)
print(*b)#prints the individual elements in the list

####tuples are used only when security is needed

