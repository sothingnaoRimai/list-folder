# b=[9,-6,4,-1,3,10,-31]
# i=0
# p=[]
# n=[]
# while i<len(b):
#     if b[i]>0:
#         p.append(b[i])
#     else:
#         n.append(b[i])
#     i=i+1
# print(p,"\n",n)
# print(50/5)


# print(149+36+196+60+113+190+225+15+31+55+45+35+15+140+140+40+112+45+40+12+12)

# print(112+196+240+113+149+55+31+80+35+45+36+225+190+60+140+140+)

b=[9,-6,4,-1,3,10,-31]
i=0
x=[]
z=[]
while i<len(b):
    if b[i]>0:
        x.append(b[i])
    elif b[i]<0:
        z.append(b[i])
    i=i+1
print(x,z)
