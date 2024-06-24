import random, sys

print("Welcome to the psych random name picker.\n")
print("A name just like sean would pick for gus.")

first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
 "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
 'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
 'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
 'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
 'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
 'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
 'Mergatroid', '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch',
 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug'
 )

middle = ( 'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
 "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
 'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
 'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
 "Winston 'Jazz Hands'", 'Worms' 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
 'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
 'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
 'Rosenthal', 'Rubbins', 'The Big News', 'Grunts', 'Tinkie Winkie'
)

last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
 'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
 'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
 'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
 'Noseworthy', 'Sackrider', 'Snuggleshine', 'Splern',
 'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
 'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
 'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
 'Woolysocks')
while True:
    firstName = random.choice(first)
    lastName = random.choice(last)
    include_middle = random.choice([True, False, False]) #1/3 chance of having middle name
    middleName = random.choice(middle) if include_middle else ""
    full_name = f"{firstName} {middleName} {lastName}".strip()
    print("\n")
    print(full_name)
    print("\n")
    try_again = input("Press any key to play again and 'E' to exit: ")
    if try_again.lower() == "e":
        break
input("Press Enter to Exit")