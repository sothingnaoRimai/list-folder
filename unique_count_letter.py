
a=["s","o","t","h","i","n","g","n","a","o"]
unique_list=[]
for each in a:
    if each not in unique_list:
        unique_list.append(each)
print("unique count is",len(unique_list))