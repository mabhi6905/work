user_input=input("enter element with,to seprate them and if they element is string then put it in double or single quote")
list_1=user_input.split(",")
list_2=[eval(x) for x in list_1]
checking=set(list_2)

if len(list_2)>len(checking):
  print("the list with unique elments",list(checking))

else:
  print("list is",list_2)