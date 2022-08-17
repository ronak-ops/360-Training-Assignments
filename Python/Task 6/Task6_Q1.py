# Write a program in Python to find out the character in a string which is uppercase using list comprehension. 


data_str = "RonakChandgadhia"
data_uppercase = [i for i in data_str if i == i.upper()]
print(data_uppercase)