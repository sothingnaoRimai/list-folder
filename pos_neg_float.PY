a=[9,-8,9.7,7,6,-5,-4,5.66,8.5,15,-5]
i=0
n=[]
b=[]
h=[]
while i<len(a):
    if (type(a[i])==float):
        n.append(a[i])
    elif a[i]<0:
        b.append(a[i])
    else:
        h.append(a[i])
    i=i+1
print(n,"is float")
print(b,"is negative")
print(h,"is positive")
