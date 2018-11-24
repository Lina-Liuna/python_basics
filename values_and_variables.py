from math import *

print(4)
print("4")
print(4+5)
print('4+5')

print(type(4))
print(type("4"))

#print(int("a"))
print(str(12345))

print("7" + "8")
#The plus operator (+) works differently for strings.

print("pi is ", 3.14, "for short")


#eval function: evaluates the passed arguments, using eval is a security hole.
#eval evaluate the passed string as a Python expression and returns the result.

#print(eval(input()))



expr = input("Enter the function(in terms of x):")
x = int(input("Enter the value of x:"))
y = eval(expr)
print("y = {}".format(y))


k = "acho"

print(locals().get(k, None))