# Write a program in Python to implement the given flowchart:


def FlowChart():
    a,b,c = 10,20,30

    avg=(a+b+c)/3
    print("Average is: ",avg)

    if avg>a and avg>b and avg>c:
        message = "Average is higher than a,b,c"
    elif avg>a and avg>b:
        message = "Average is higher than a,b"
    elif avg>a and avg>c:
        message = "Average is higher than a,c"
    elif avg>b and avg>c:
        message = "Average is higher than b,c"
    elif avg>a:
        message = "Average is just higher than a"
    elif avg>b:
        message = "Average is just higher than b"
    elif avg>c:
        message = "Average is just higher than c"
    print(message)
    return None

FlowChart()