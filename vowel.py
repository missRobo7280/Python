a=input()
c=0
for i in a:
    if i in 'aeiouAEIOU':
        c+=1        

s=a[-1]
if s not in 'AEIOUaeiou':
    c+=1
        
print(c)
    
