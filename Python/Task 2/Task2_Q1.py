# Write a program in Python to perform the following operation:
# -If a number is divisible by 3 it should print “Consultadd” as a string
# -If a number is divisible by 5 it should print “Python Training” as a string
# -If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string


x = 15
if (x%3)==0 and (x%5)==0:
    print("Consultadd - Python Training")

elif (x%5)==0:
    print("Python Training")

elif (x%3)==0:
    print("Consultadd")

else:
     print("Contact Rujul")
