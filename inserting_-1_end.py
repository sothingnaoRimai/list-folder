a=[11,1,13,14,15,10]
i=0
b=[]
while i<len(a):
    if (a[i]>11):
        b.append(a[i])
    i=i+1
b.insert(0,-1)
b.insert(5,-1)
print(b)