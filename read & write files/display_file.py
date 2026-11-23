# This program displays the contents
# of a file.

infile = open('copy.txt', 'r')

file_contents = infile.read()

infile.close()
print(type(file_contents))

print(file_contents)
