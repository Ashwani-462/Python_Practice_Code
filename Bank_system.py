#Bank system
print("                    Hello sir/madam welcome to the bank                  ")
print("                   Please sign in first for our services                  ")
print("--------------------------------------------------------------------------")
username=input("Enter your username: ")
password=input("Enter your password: ")
amo=float(input("Enter the amount to deposit: "))
print("                Your amount has been deposited successfully               ")
print("--------------------------------------------------------------------------")
print("                     login to your account                     ")
user1name=input("Enter your username: ")
user1pass=input("Enter your password: ")
if(username==user1name and password==user1pass):
    print("Login successful")
    print("Your current balance is: ",amo)
else:
    print("Login failed")
oper=(input("What operation do you want to perform? 1.Withdrawal 2.Deposit 3.Check Balance :"))
if(oper=="Withdrawal" or oper=="withdrawal"):
    wid=float(input("Enter the amount to withdraw: "))
    if(wid>amo):
        print("Insufficient balance")
    else:
        amo=amo-wid
        print("Please collect your cash")
        print("Your current balance is: ",amo)
elif(oper=="Deposit" or oper=="deposit"):
    dep=float(input("Enter the amount to deposit: "))
    amo=amo+dep
    print("Your amount has been deposited successfully")
    print("Your current balance is: ",amo)  
elif(oper=="Check Balance"):
    print("Your current balance is: ",amo)
else:
    print("Invalid operation")
