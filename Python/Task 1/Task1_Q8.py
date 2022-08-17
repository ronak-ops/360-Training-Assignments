# If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. 
# Will it change the value? If Yes then Why?

# --Explanation:
# --Yes, variables in Python can be reassigned to a new value that is a different data type from its current value.
# --In fact, variables can be reassigned to any valid value in Python, regardless of its current value.
# --Variables are essentially like an empty box, that can contain something like a string, number, or other value. 
# --When you assign it a value, the box will contain that value, and when you reassign it, it will empty out the old value, and the new value will be placed inside of it.
# --Therefore Python is known as a dynamically typed programming language.


#This variable is initially assigned as a string.
x = 'Consultadd'
print(x)
#It can be reassigned to any other value, regardless of the type.
x = 25
print(x)
