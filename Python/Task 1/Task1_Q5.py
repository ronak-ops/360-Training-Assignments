# Write a program to complete the task given below: Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the sum in another variable called z. Add 30 to z and store the output in variable result and print result as the final output.


x = int(input("Enter any number between 1 and 10: "))
y = int(input("Enter other number between 1 and 10: "))
z = x+y
result = z+30
print("The final output is: ", result)
