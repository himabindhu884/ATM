print("Maximum 16 charecters")
user=(input("Enter uppercase latters"))
user1=(input("Enter lowercasa latters"))
num=int(input("Enter number"))
d=(input("Enter the symbal"))
if user>"A" and user<"Z":
    char1=user
    if user1>="a" and user1<"z":
        char2=user1
        if num>=0 and num<=9:
            char3=str(num)
            if d in ("@","#","!","?","$","&"):
                char4=d
            print(char1+char2+char3+char4)