#function homework
#use validation function
#ask the user for hours and minutes
def validate_time(hours, minutes):
    while hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        print('Invalid time. Please enter valid hours and minutes.')
        hours = int(input('Enter a value between 0 and 23: '))
        minutes = int(input('Enter a value between 0 and 59: '))

    return hours, minutes
#call the validation function
def main():
    hours = int(input('Enter a value between 0 and 23: '))
    minutes = int(input('Enter a value between 0 and 59: '))

    hours, minutes = validate_time(hours, minutes)

    print(f'Hours: {hours}')
    print(f'Minutes: {minutes}')

main()
                    
    
