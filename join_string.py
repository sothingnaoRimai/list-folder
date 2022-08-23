a=["A","T","O","M"," ","B","O","M","B"]
i=0
s=''
while i<len(a):
    j=0
    while j<len(a[i]):
        s+=a[i][j]
        j=j+1
    i=i+1
print(s)