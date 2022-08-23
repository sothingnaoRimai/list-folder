a=['a','b',['c',['d','e'],['f','g'],'h'],'i','j']
i=0
c=[]
e=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        b=a[i][j]
        c.append(b)
        j=j+1
    i=i+1
k=0
while k<len(c):
    l=0
    while l<len(c[k]):
        d=c[k][l]
        e.append(d)
        l=l+1
    k=k+1
print(e)