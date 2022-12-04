# Question1
# write a funtion to print max of given number
def finfmaxofthreenumbers(num1,num2,num3):
    if(num1>num2 and num1 >num3):
      print("greatest number : ",num1)
    elif (num2 >num1 and num2 >num3):
      print("greatest number :",num2)
    else:
      print("greatest number :",num3)
n1=int(input("Enter number1:"))
n2=int(input("Enter number 2:"))
n3=int(input("Enter number 3:"))

finfmaxofthreenumbers(n1, n2, n3)