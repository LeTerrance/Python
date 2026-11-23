#Chapter 5 practice
#get the number from user
def get_input():
    number = float(input('Enter a positivie number(negative to quit): '))
    return number
#adds numbers to the running total
def add_numbers(total,number):
    total += number
    return total
#displays final total
def print_output(total):
    print('The total is:', total)
#controls program and loops the other functions
def main():
    total = 0

    number = get_input()
#negative number ends the loop
    while number >= 0:
        total = add_numbers(total, number)
        number = get_input()

    print_output(total)

main()
