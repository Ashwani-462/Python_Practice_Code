#Code for calculator 
print("Enter your Numbers")
num1=float(input("Enter your first number: "))
num2=float(input("Enter your second number: "))  
op=input("Chose your operator (+,-,*,/)=")
if(op== "+"):
    print("The sum of numbers is ",num1+num2)
elif(op== "-"):
    print("The subtracion of numbers is ",num1-num2)
elif(op== "*"):
    print("The multiplication of numbers is ",num1*num2)
else:
    print("The division of numbers is ",num1/num2)
