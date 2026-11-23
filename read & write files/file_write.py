# This program writes three lines of data
# to a file.
def main():
    # Open a file named philosophers.txt.
    outfile = open('philosophers.txt', 'w')

    # Write the names of three philosphers
    # to the file.
    outfile.write('Socrates\n')
    outfile.write('Aristotle\n')
    outfile.write('Andrew Tate\n')

    # Close the file.
    outfile.close()

# Call the main function.
if __name__ == '__main__':
    main()
