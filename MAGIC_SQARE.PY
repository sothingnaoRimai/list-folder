magic_square=[[8,8,4],[5,5],[2,3,1]]
# print (type (magic_square))
# print (type (magic_square))
# print (type (magic_square))
# print (sum (magic_square[2]))
# print (sum (magic_square[1]))
# print (sum (magic_square[0]))
# place=["delhi","gujarat","rajasthan","punjab"]
# i=1
# while i<len(place):
#     print(place[-i])
#     i=i+1
# s=[50,60,9,11,13,20,6]
# i=0
# while i<len(s):
#     if (s[i]>9):
#         print(s[i])
#     i=i+1
# n=[50,40,23,70,39]
# i=1
# while i<len(n):
#     if (n[i]>20) and (n[i]<40):
#         print(n[i])
#is     i=i+1
# list1=[[1,3,5,7][2,4][8,9,10]]
# print(list1[0][0])
# # a=[[5,9][4[6,2],1,2]]
# # print(a[1])

 a=[[1,2,3,],5,6,12,[0],[5,6]]
# print(a[0][0])
# print(a[0][2])
# print(a[3])
# print(a[4][0])
# print(a[5][0])

# a=[[1,3,5,7][2,4][8,9,10]]
# print(a[0][0])
# print(a[0][2])
# print(a[])

# list1=[1,-1,2,-2,-5,-6]
# print(list1[1])
# print(list1[3])
# print(list1[4])
# print(list1[5])

# lid=["one","two","three","four"]
# print(lid[1])
# print(lid[3])

# m_sq=[[8,3,4],[1,5,9],[6,7,2]]
# i=0
# while i<len(m_sq):
#     r=0
#     c=0
#     j=0
#     while j<len(m_sq):
#         r=r+m_sq[i][j]
#         c=c+m_sq[j][i]
#         d=0
#         while d<len(m_sq):
#             d1=0
#             d2=0
#             c1=0
#             while c1<len(m_sq):
#                 d1=d1+m_sq[d][c]
#                 d2=d2+m_sq[c][d]
#                 d1=d2
#                 c=c+1
#             d=d+1
#         j=j+1
#     i=i+1
# print("row",r)
# print("column",c)
# print("decimal",d)
# if r==c==d:
#     print("it is magic square")
# else:
#     print("it is not a magic square")

magic_square =[[8, 3, 4],[1, 5, 9],[6, 7, 2]]
i=0
while i<len(magic_square):
    row=0
    column=0
    j=0
    while j<len(magic_square):
        row=row+magic_square[i][j]
        column+=magic_square[j][i]
        d=0
        while d<len(magic_square):
            d1=0
            d2=0
            c=0
            while c<len(magic_square):
                d1=d1+magic_square[d][c]
                d2=d2+magic_square[c][d]
                d1=d2
                c=c+1
            d=d+1
        j=j+1
    i+=1
print("row",row)
print("column",column)
print("Decimal",d1)
        
if column==row==d1:
    print(" It is a magic square")
else:
    print("Not a mag")