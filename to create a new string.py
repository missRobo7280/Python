#program to generate a new string using the previous string by printing the even and then the odd elements
a=input()
s=''
for i in range(0,len(a),2):
    s+=a[i]
for i in range(1,len(a),2):
    s+=a[i]
print(s)

#second method:
a=input()
s1=''
s2=''
for i in range(0,len(a)):
    if i%2==0:
        s1+=a[i]
    else:
        s2+=a[i]
print(s1+s2)

#third method
a=input()
print(a[::2]+a[1::2])



