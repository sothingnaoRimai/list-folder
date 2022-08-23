a=[3000,60000,897035647,468976540,300000,675389065,6759,87865,987654,246757]
i=0
n=[]
m=[]
o=[]
while i<len(a):
    if (a[i])<100000:
        n.append(a[i])
    elif (a[i])<10000000:
        m.append(a[i])
    else:
        o.append(a[i])
    i=i+1
print(n,"dilwale")
print(m,"lakhpati")
print(o,"crorepati")