def factorial(num):
    if num == 0:
        return 1
    else:
        return(num* (factorial(num-1)))
num=int(input("Enter the number"))
result=factorial(num)
print("The factorial of",num,"is",result)