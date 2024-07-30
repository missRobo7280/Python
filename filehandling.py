f=open(r'C\Users\Swati\Downloads\cars.csv,'r')
b=f.readlines()
res=[]
for i in b:
    arr=list(i,split(','))
    if arr[-1]not in res:
        res.append(arr[-1])
        print(len(res))
f.close
             
