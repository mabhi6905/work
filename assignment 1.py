n=int(input("number of student"))

student_names=[]
student_roll_no=set()
student_percentage=[]
student_year=[]
student_details={"name":student_names,"roll_no":student_roll_no,"percentage":student_percentage,"year":student_year}


for i in range(n):
  i=input("name of student")   
  student_names.append(i)

  i=int(input("roll no of student"))
  student_roll_no.add(i)
  

  i=float(input("percentage of student"))
  student_percentage.append(i)

  i=eval(input("YEAR of student"))   
  student_year.append(i)

def roll_no():
  print(student_names)
  revised_roll=input("correct roll no.")
  list1=revised_roll.split(",")
  lres = [int(x) for x in list1]
  
  student_roll_no.update(lres)
    
  
j=1
while len(student_names)>len(student_roll_no):

  
  if j==1:
    print("student roll no. should be unique")
   
  else:
     print("entered value is again wrong")
  
  roll_no()
  j+=1
 
  
else:
  print(student_details)