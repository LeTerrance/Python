#Ask the user for sales numbers for 7 days.
#Use a for loop  to add the sales numbers
#and then use a while loop to add the numbers.
#Make a note of the differences 


#Ask the user for sales numbers for 7 days.
x = 1
sales = 0

#Use a for loop  to add the sales numbers
for day in range(7):
    sales_numbers = float(input('What are the sales for today?: '))
    sales += sales_numbers
    while x >= 7:
        sales_add = float(input('What are the numbers for each sale today?: '))
        sales += sales_add
print(f'Total numbers this week', sales)
        
    



    
