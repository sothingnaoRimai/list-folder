a=[[1,2],[5,8],[4,7],[3,9]] 
i=0
b=[]
c=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        e=a[i][j]
        if e%2==0:
            b.append(e)
        j=j+1
    i=i+1
print(b)
