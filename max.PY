# a=[5,6,10,1,0,7,9]
# a=[5,6,10,1,0,7,9]
# i=0
# while i<len(a):
#     i=i+1
# print("the greatest",a[2])
# print("the smalles/t",a[4])

a=[5,6,10,1,0,7,900]
i=0
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
print(max)