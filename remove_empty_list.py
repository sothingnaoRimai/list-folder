
list1=[1,2,3,[],4,[],5]
i=0
s=[]
while i<len(list1):
    if list1[i]!=[]:
        s.append(list1[i])
    i=i+1
print(s)