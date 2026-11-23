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
#decimal placement
print (f'{num:,.2f}')
#precision
print (f'{num:.2%}')
#adds comma to number
print (f'{num2:,d}')
#format with numbers
print (f'The number is {num:12,.2f}')
#align left
print(f'{num:<20.2f}')
#align right
print(f'{num:>20.2f}')
#align middle
print(f'{num:^20.2f}')

