a=[1,3,7,5,6,8,2,4,19,40,10]
i=0
sum=0
total=0

while i<len(a):
    avg1=0
    if (a[i]%2==0):
        sum=sum+(a[i])
        avg1=sum/len(a)
    elif (a[i]%2!=0):
        total=total+(a[i])
        avg=total/len(a)
    i=i+1
print("sum of all even",sum)
print("sum of all odd",total)
print("average of even",avg1)
print("average of odd",avg)

