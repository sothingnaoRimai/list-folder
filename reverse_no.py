user=int(input("enter no: "))
b=str(user)
i=-1
s=" "
while i>=-len(b):
    s=s+b[i]
    i=i-1
print(s)