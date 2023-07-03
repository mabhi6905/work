user_input=input("enter element with,to seprate them and if they element is string then put it in double or single quote")
list_1=user_input.split(",")
list_2=[eval(x) for x in list_1]
occurrence = {x: list_2.count(x) for x in list_2}

for i in range(len(list_2)):
  print(list_2[i],occurrence.get(list_2[i]))