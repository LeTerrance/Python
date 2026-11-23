#ch3 practice
'''Children under 3 years old: Free admission
Children aged 3 to 12: $10 per ticket
Students: $15 per ticket
Adults aged 13 to 64: $20 per ticket
Seniors aged 65 and above: $12 per ticket'''

age = int(input('Enter your age: '))
student = input('Are you a student? (yes/no): ')

if age < 3:
    price = 0
elif student == "yes":
    price = 15
elif age <= 12:
    price = 10
elif age <= 64:
    price = 20
else:
    price = 12

print ('Your ticket price is $' + str(price))


               
               

    
        




