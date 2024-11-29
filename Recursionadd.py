def addition(num1,num2):
    if num2==0:
        return num1
    else:
        return addition(num1+1,num2-1)
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
result=addition(num1,num2)
print("the sum of the numbers entered is:",result)
