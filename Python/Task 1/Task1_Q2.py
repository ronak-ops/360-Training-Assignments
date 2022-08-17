# Create a variable of type complex and swap it with another variable of type integer.


x = eval(input("Enter the value of x: "))
y = eval(input("Enter the value of y: "))

x,y = y,x
print("The value of x after swapping: =", x)
print("The value of y after swapping: =", y)
print(type(x))
print(type(y))