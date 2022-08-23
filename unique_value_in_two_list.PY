list1=[9,2,3,99,5,6,7,13]
list2=[1,2,3,4,5,7,6]
i=0
a=[]
while i<len(list1):
    if list1[i] in list2:
        a.append(list1[i])
    i=i+1
print(a)


# list1=["a","p","y"]
# list2=["u","a","t"]
# i=0
# a=[]
# while i<len(list1):
#     if list1[i] in list2:
#         a.append(list1[i])
#     i=i+1
# print(a)