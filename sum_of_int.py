p=["iuytf",9.7,55,"98765",45,5.8765]
i=0
sum=0
while i<len(p):
    if (type(p[i])==int):
        sum=sum+p[i]
    i=i+1
print(sum)


a=[1,3,7,5,6,8,2,4,19,40,10]
i=0
sum=0
while i<len(a):
    if (a[i]%2==0):
        sum=sum+(a[i])
    i=i+1
print(sum)