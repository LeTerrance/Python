#Loops chp 4 practice problem


#Have a hard-coded password (for example "password").
password = 'password'

attempts = 0
#Ask the user to enter the password.
#Give the user up to 3 attempts to enter the correct password.
#If the user enters the correct password within 3 attempts, display “Access granted.” and stop.
while attempts < 3:
    user_password = input('Enter the password: ')

    if user_password == password:
        print('Access granted.')
        break

    attempts += 1
#If the user fails all 3 attempts, display “Account locked".
if attempts == 3:
    print('Account locked.')
 
