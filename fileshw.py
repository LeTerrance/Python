# Write a program that reads the attached file numbers.txt
# display the sum and average of numbers stored in the file.
def main():
    total = 0
    count = 0
    
    with open('numbers.txt','r') as file:
        for line in file:
            number = float(line)
            total+= number
            count += 1

    if count > 0:
        average = total / count
        print(f'Sum: {total}')
        print(f'Average: {average}')
    else:
        print('The file contains no numbers.')

main()

        

