my_list=[[1, 2], [3,4], [3, 5], [6]]

for i,sub_list in enumerate(my_list):
  for j,elem in enumerate(sub_list):
    if elem==3:
      my_list[i][j]=3

print(my_list[-i])