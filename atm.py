print("welcome to ATM")
print("Insert your card here")
print("Enter the language")
pin=int(input("Enter the 4 digit number"))
amt=25000
if pin==2001:
    print("1.balance enquiry")
    print("2.withdraw")
    print("3.deposit")
    print("4.change your pin")
    print("5.transfer of money")
    print("6.quit")
    choose=int(input("enter the transaction"))
    if choose==2:
        k=int(input("enter the amount"))
        if k>2000:
            print("withdraw amount")
        else:
            print("valid amount")
    elif choose==3:
        b=int(input("enter the deposit amount"))
        if b>2000:
            print("successfully deposited")
        else:
            print("valid amount")