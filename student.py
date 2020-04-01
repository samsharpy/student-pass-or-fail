#created 21/10/2019
#author : samuvel
a=str(input('enter the name of the student:'))
b=int(input('enter the average of the student:'))
c=int(input('enter the class of the student:'))# geting student details
b=b*5# finding total marks
if (b>199):
      print("congrats")#checking whee pass
      print("student promoted to class",c+1)
elif(b>500):
      print("average is wrong check the data")#or wrong input
else:# or fail
    print ("the student failed")
if (b>199):
    d=c+1
    d="student passed to class:",d
else:
    d=c
    d="student failed remains in class:",d
b=("Mark scored by the student is",b) 
list=[a,b,d]
for x in list:
      print(x)#printing all the outputs
