a=[" "]
b=[]
i=0
while i<len(a):
    if a[i] in b:
        b.append(a[i])
    i=i+1
print(b,"a is an empty list")
