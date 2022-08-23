lit=[2,3,2,4,5,6,7,5]
i=0
a=[]
while i<len(lit):
    if lit[i] not in a:
        a.append(lit[i])
    i=i+1
print(a)
