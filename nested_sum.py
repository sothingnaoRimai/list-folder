a=[[33,75,45],[76,87,99],[78,45,67]]
i=0
sum=0
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
    i=i+1
print(sum)