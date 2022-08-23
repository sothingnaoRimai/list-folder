a= input("enter name?")
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    print(v,end=" ")sum_nested.py
    