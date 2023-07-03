import keyboard
user_input=int(input("enter the number of which you want factorial and fibonachi "))

def fac(n):
  factorial=1
  for i in range(1,n+1):
    factorial= factorial*i

  print(factorial)
    
def fibonaci(n):
  if n<=1:
    return n
  else:
    return (fibonaci(n-1)+fibonaci(n-2))
 
  for i in range(user_input):
   print(fibonaci(i))


what_user_want=int(input("0 for factorial ,1 for fibonachi"))
if what_user_want==0:
  fac(user_input)
elif what_user_want==1:
  fibonaci(user_input)
else :
  print("enter 0 or 1")

  
