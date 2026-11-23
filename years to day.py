#Create a program that takes the age in years and returns the age in days.

#Ask how old the person in
age_years = float(input('How old are you?: '))

#Calculate the age in days
days = 365
age_days = int(age_years * days)

#Display results
print(f'You are {age_days:12,}')
