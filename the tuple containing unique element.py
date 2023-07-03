user_input=input("enter element with,to seprate them")
tuple_1=tuple(user_input.split(","))
checking=set(tuple_1)

if len(checking)<len(tuple_1):
  print("the tuple contain one or more then one same elment")
  print("unique elments present in the tuple is ",tuple(checking))
  

else:
  print("tuple has unique elements",tuple_1)
