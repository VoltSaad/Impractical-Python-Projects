'''
ask user for a word
check if its vowel or not
if its vowel:
    add way to the end of the word
else:
    take the first word, take it to the end and add 'ay'

ask user to play again or quit
'''

'''
the code I wrote
word = input("Input a word to be converted to Pig Latin: ")

def starts_with_vowel(word):
    vowels = 'AEIOUaeiou'
    return word[0] in vowels

while True:
    if starts_with_vowel is True:
        print(f"{word}way")
    else:
        word[1:]+word[0]
        print(f"{word}ay")
    try_again = input("Press any key to play again or 'E' to Exit: ")
    if try_again.lower() == 'e':
        break
'''

#GPT code
print("Press Enter again to exit: ")

def starts_with_vowel(word):
    vowels = 'AEIOUaeiou'
    return word[0] in vowels

while True:
    word = input("Input a word to be converted to Pig Latin: ")

    if starts_with_vowel(word):
        print(f"{word}way")
    else:
        pig_latin_word = word[1:] + word[0] + "ay"
        print(pig_latin_word)
        
    try_again = input("Press any key to play again or 'E' to Exit: ")
    if try_again.lower() == 'e':
        break

#solution by book
"""Turn a word into its Pig Latin equivalent.
import sys

VOWELS = 'aeiouy'

while True:
    word = input("Type a word and get its pig Latin translation: ")

    if word[0] in VOWELS:
        pig_Latin = word + 'way'
    else:
        pig_Latin = word[1:] + word[0] + 'ay'
    print()
    print("{}".format(pig_Latin), file=sys.stderr)
    
    try_again = input("\n\nTry again? (Press Enter else n to stop)\n ")
    if try_again.lower() == "n":
        sys.exit()

"""