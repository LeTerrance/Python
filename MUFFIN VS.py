#You work for a bakery that sells two items: muffins and cupcakes.
#The number of muffins and cupcakes in your shop at any given time is stored in the variables muffins and cupcakes
#the store has 10 muffins and 10 cupcakes.
#Write a program that takes strings from standard input indicating what your customers are buying ("muffin" for a muffin, "cupcake" for a cupcake).
#If they buy a muffin, decrease muffins by one, and if they buy a cupcake, decrease cupcakes by 1.
#If there is no more of that baked good left, print ("Out of stock").
#Once you are done selling, input "0", and have the program print out the number of muffins and cupcakes remaining, in the form "muffins: 9 cupcakes: 3"


muffins = 10
cupcakes = 10

choice = input('What would you like to buy?: ')

while choice != '0':
    parts = choice.split()

    quantity = int(parts[0])
    item = parts[1]

    if item == 'muffins':
        if quantity <= muffins:
            muffins -= quantity
            print('Purchase successful!')
        else:
            print("Sorry, we're out of muffins.")
            
    elif item == 'cupcakes':
        if quantity <= cupcakes:
            cupcakes -= quantity
            print('Purchase successful!')
        else:
            print("Sorry, we're out of cupcakes")
         
    choice = input('What would you like to buy?: ')

print('muffins:', muffins)
print('cupcakes:', cupcakes)

