#Design a program that lets the user enter the total rainfall for each of 12 months into a list. 
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, and the months names with the highest and lowest rainfall

def main():
    #List to store rainfall data
    rainfall = []
    #List of month names
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    #Get rainfall data from user
    for month in months:
        while True:
            try:
                rain = float(input(f'Enter the total rainfall for {month}: '))
                rainfall.append(rain)
                break
            except ValueError:
                print("Please enter a valid number.")

    #Calculate total and average rainfall
    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / len(rainfall)
    #Find the month with the highest and lowest rainfall
    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    max_month = months[rainfall.index(max_rainfall)]
    min_month = months[rainfall.index(min_rainfall)]
#Display results
    print(f'\nTotal rainfall for the year: {total_rainfall:.2f} inches')
    print(f'Average monthly rainfall: {average_rainfall:.2f} inches')
    print(f'Month with the highest rainfall: {max_month} ({max_rainfall:.2f} inches)')
    print(f'Month with the lowest rainfall: {min_month} ({min_rainfall:.2f} inches)')
#Call the main function
if __name__ == '__main__':
    main()
