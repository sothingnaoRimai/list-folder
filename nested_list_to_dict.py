
my_list=[['fruit','apple','banana','grapes'],['color','red','blue'],['animal','dog']]

result={}
for sub_list in my_list:
  result[sub_list[0]]=sub_list[1:]
print(result)