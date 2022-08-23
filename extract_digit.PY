
a='manisha 4534 @navgurukul'
i=0
b=a.split()
while i<len(b):
    if b[i].isdigit():
        print(b[i])
    i=i+1