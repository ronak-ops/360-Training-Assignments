# Write a program in Python to perform the following operator	 based task:
# -Ask user to choose the following option first: 
# •	If User Enter 1 - Addition 
# •	If User Enter 2 - Subtraction 
# •	If User Enter 3 - Division 
# •	If User Enter 4 - Multiplication 
# •	If User Enter 5 - Average 
# -Ask user to enter two numbers and keep those numbers in variables num1 and num2 respectively for the first 4 options mentioned above. 
# -Ask the user to enter two more numbers as first and second for calculating the average as soon as the user chooses an option 5. 
# -At the end if the answer of any operation is Negative print a statement saying “NEGATIVE” 
# -NOTE: At a time a user can only perform one action. 


def Operations():

    list=[1,2,3,4]
    optr = int(input("Enter 1 for Addition, 2 for Subtraction, 3 for Division, 4 for Multiplication and 5 for Average: "))
    if optr in list:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
    if optr==1:
            output = num1+num2

    elif optr==2:
            output = num1-num2

    elif optr==3:
            output = num1/num2

    elif optr==4:
            output = num1*num2

    elif optr==5:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            num3 = int(input("Enter third number: "))
            num4 = int(input("Enter fourth number: "))
            output = (num1+num2+num3+num4)/4
    print("Result is : ", output)
    if output<0:
            print("Result is NEGATIVE")
Operations()
