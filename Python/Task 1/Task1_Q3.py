# Swap two numbers using a third variable and do the same task without using any third variable.


x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

temp = x
x = y
y = temp

print("The value of x after swapping: ", x)
print("The value of y after swapping: ", y)
