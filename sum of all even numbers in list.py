digits=input("enter numbers with,to seprate them")
numbs=digits.split(",")
numbers=[int(x) for x in numbs]
print((numbers))
sum=0
for i in range(len(numbers)):
  if numbers[i]%2==0:
    sum=sum+numbers[i];

print("sum of all the even numbers present in list is",sum)
    