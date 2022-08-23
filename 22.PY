#  # output-491625
a=[2345]
i=0
b=[]
n=" "
while i<len(a):
    j=0
    while j<len(a[i]):
        e=a[i]
        j=e%10
        n=str(j*j)+n
        j=j+1
    i=i+1
print(n)

