#A SIMPLE CALCULATOR WHICH TAKES TWO NUMBERS AS INPUT FROM THE USER AND ASK THE USER TO CHOOSE THE ARITHMETIC OPERATIONS TE USER WANTS TO PERFORM ZND THEN GIVESTHE DESIRED OUTPUTS.
num1=int(input("Enter first number :"))
num2=int(input("Enter second number:"))

print(" Choose the Arithmetic operator on which you want to perfrom arithmetic operation:\n  1.Addition(+) \n 2. Subtraction(-) \n 3. Multiplication(*) \n 4. Division(/) \n 5. Floor Division(//)\n 6. Modulo(%)\n")
choice=int(input("1.Select operation from 1,2,3,4,5,6:"))
print("Enter two numbers for arithmetic operations:")

if choice == 1:
    print("You have chosen (+) operator")
    print(num1 ,"+",num2,"=" ,":", num1+num2)
elif choice == 2:
    print("You have chosen (-) operator")
    print(num1 ,"-", num2 ,"=",":", num1-num2)
elif choice == 3:
    print("You have chosen (*) operator")
    print(num1 ,"*", num2 ,"=",":", num1*num2)
elif choice == 4:
    print("You have chosen (/) operator")
    print(num1 ,"/", num2 ,"=",":", num1/num2)
elif choice == 5:
    print("You have chosen (//) operator")
    print(num1 ,"//", num2 ,"=",":", num1//num2)
elif choice == 6:
    print("you have chosen (%) operator")
    print(num1 ,"%", num2 ,"=",":", num1%num2)
else:
    print("Invalid step")

    
    
    
