#various formatting options. Optional you can ignore
import math


''' The % between "%.2f" and number serves as a string interpolation
operator in this context. The %inside the string "%.2f" signifies that the .2f
is part of a format specifier. '''

x = 3.445
y = "joe"

print('%.2f' % (3.445))
print('%.2f' % (x))
print("________")

print("hello %s. The number is %s" %(y,x))
print("hello %s. The number is %d" %(y,x))
print("hello {a}. The number is {b}".format(a=y,b=x))

print("________")

#using f string
print (f'{x:.2f}')
print("________")

#using string.format
print("hello {}. The number is {}". format(y,x))


y="{z:.2f}"
print(y.format(z=3.445))
print("{z:.2f}".format(z=3.445))


