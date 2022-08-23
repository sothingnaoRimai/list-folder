# p=[[78,98],[26,48],[10,77]]
p=[[100,100],[200,100],[10,100]]
i=0
sum=0
while i<len(p):
    j=0
    while j<len(p[i]):
        sum=sum+p[i][j]
        j=j+1
    i=i+1
print(sum)


