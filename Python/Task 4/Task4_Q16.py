# What is the output of the following codes: 
# Scenario 1:
def foo():
    try:
        return 1
    finally:
        return 2


k = foo()
print(k)

# Scenario 2:
def a():
    try:
        f(x, 4)

    finally:
       print('after f')
    print('after f?')
a()
