##print ("100/n200")

#how to write fstrings- [alignment] [width] [,] [.precision] [type]
num = 123456.123456
num2 = 123456
print ("The number to 2 decimal places is", num)
print (f'The number to 2 decimal places is {num}')
print (f'The number to 2 decimal places is {num:.2f}')
#fstring - format string
#alignent - [^ < >]
#width - spaces
print (f'{num:,.2f}')
