my_list=[[1,2,3],[3,4,5]]
for sub_list in my_list:
  for elem in sub_list:
    if elem==3:
      sub_list.remove(3)
print(my_list)