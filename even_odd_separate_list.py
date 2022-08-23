# [6, 10, 0]
# [5, 1, 7, 9]
a=[5,6,10,1,0,7,9]
i=0
n=[]
m=[]
while i<len(a):
    if (a[i]%2==0):
        n.append(a[i])
    else:
        m.append(a[i])
    i=i+1
print(n)
print(m)




