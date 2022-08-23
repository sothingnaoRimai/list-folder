b=[9,-6,4,-1,3,10,-31]
i=0
p=[]
n=[]
while i<len(b):
    if b[i]>0:
        p.append(b[i])
    else:
        n.append(b[i])
    i=i+1
print(p,"\n",n)