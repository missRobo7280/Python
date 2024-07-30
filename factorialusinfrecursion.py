def sample(n):
    if n==1:
        return 1
    return n+sample(n-1)
    #5*sample(4),5*4*sample(3),5*4*3*sample(2),5*4*3*2*sample(1),5*4*3*2*1=120
n=int(input())
print(sample(n))
