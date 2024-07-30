#return the number of two consecutive consonant combinatons
a=input()
c=0
v='aeiouAEIOU'
for i in range(len(a)-1):
    if(a[i] not in v )and (a[i+1] not in v):
       c+=1
print(c)
                        
