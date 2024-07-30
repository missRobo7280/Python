s=input()
count=0
for i in s:
    if i in '0123456789':
        count+=1
print(count)
#or we can also use the ASCII values by using "ord"
##if ord(i)>=48 and ord(i)<=57:
c=0
for i in s:
    if i.isdigit():
        c+=1
print(c)
