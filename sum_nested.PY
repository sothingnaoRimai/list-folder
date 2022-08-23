# a=[10,10,[20,30],[90,40],20,10]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a([i][j])
#         j=j+1
#     i=i+1
# print(sum)


# a=[[20,30],[90,40],[20,10]]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         sum=sum+a[i][j]
#         j=j+1
#     # sum=sum+total
#     i=i+1
# print(sum)

a=[[10,20],[30,20],[40,30]]
i=0
sum=0
while i<len(a):
    j=0
   
    while j<len(a[i]):
        sum+=a[i][j]
        j=j+1
    i=i+1
print(sum)