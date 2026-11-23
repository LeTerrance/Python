#print end and sep and newline and tab
print("one")
print("two")
print("one", "two")

print("one", "two", end = '*')
print()
print("one", "two", sep = '*')
#print()
print("100\n200")
print("100\t200")
 

#how to write fstrings-[alignment][width][,][.precision][type]
num = 123456.123456
num2 = 123456
print(f'{num:.2f}')
print(f'{num:,.2f}') 
print(f'{num:.2%}')
print(f'{num2:,d}')
print(f'The number is {num:12,.2f}')
print(f'{num:<20.2f}')
print(f'{num:>20.2f}') 
print(f'{num:^20.2f}')

