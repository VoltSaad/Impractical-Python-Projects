'''start with 2 lists
first list to be for first names and second list for funny names
use tuple 

pseudo code

Load a list of first Name
Load a list of surnames
choose the first name at random
assign the name to a variable
choose a surname at random
assign the name to a variable
print the names on the screen in order and in red font 
ask the user to quir or play again
IF user play again:
    repeat
if user quits:
    end and exit'''

import random, sys

print("Welcome to the psych random name picker.\n")
print("A name just like sean would pick for gus.\n")

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
 "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
 'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
 'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
 'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
 'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
 'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
 'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
 'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
 "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
 'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
 'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
 "Winston 'Jazz Hands'", 'Worms')

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
 'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
 'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
 'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
 'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
 'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
 'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
 'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
 'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
 'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
 'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
 'Woolysocks')

# while True:
#     firstName = random.choice(first)
#     lastName = random.choice(last)

#     print("\n\n")
#     print(f"{firstName}{lastName}", file=sys.stderr)
#     print("\n\n")
#     try_again = input("\n\n Try Again? (Press P to play and E to exit)\n")
#     if try_again.lower() == "e":
#         break
# input("\nPress Enter to exit.")    

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)
    print("\n")
    print(f"{firstName}{lastName}\n")
    try_again = input("Press any key to play again and 'E' to exit: ")
    if try_again.lower() == "e":
        break
input("Press Enter to Exit")