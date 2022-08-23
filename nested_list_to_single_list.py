a=[[7,9],[9,8,7],[9,5,2]]
i=0
b=[]
c=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        e=a[i][j]
        b.append(e)
        j=j+1
    i=i+1
print(b)