
lit=['a','b','a','c','e']
i=0
a=[]
while i<len(lit):
    if lit[i] not in a:
        a.append(lit[i])
    i=i+1

print(a)
