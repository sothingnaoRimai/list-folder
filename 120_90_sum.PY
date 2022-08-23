a=[6,1,3,5,6,3,2]  #120 90
b=[]
i=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
print(b)

j=0
t=1
sum=0
while j<len(b)-1:
    t=t*b[j]
    sum=sum+t
    j=j+1
print(t)
print(sum)