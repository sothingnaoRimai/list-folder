a=[20,49,32,76,98,33,29]
i=0
b=[]
while i<len(a):
    if a[i]>20 and a[i]<40:
        b.append(a[i])
    i=i+1
print(b)