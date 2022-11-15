import os
import random

os.system('clear')

#das ist die liste der wörter/sätze die gesucht werden
words = ['der preis is heiss', 'kuchen']

word = random.choice(words)

print("Buchstabe?")

guesses = ''
falschebuchstaben = ''
 
# wenn man möchte, kann man hier max mögliche versuche eingeben
turns = 100

while turns > 0:
 
    # wie oft lag man falsch?
    failed = 0
 
    
    for char in word:
 
        # vergleich buchstaben
        if char in guesses:
            print(char, end=" ")
 
        else:
            print("_", end=" ")
 
            #zählt falsche eingaben
            failed += 1
 
    if failed == 0:
        os.system('clear')
        # du gewinnst
        print("\n") 

        print("+++ DU GEWINNST +++")
 
        
        print("\n") 

        print("Der gesucht Ausruck lautete: ", word)
        break
 
    # falscher buchstabe eingeben, dann wird nochmal geraten
    print()
    guess = input("Dein Buchstabe lautet: ")
 
    # guesses enthällt buchstaben
    guesses += guess

 
    # checken ob buchstabe vorhanden ist
    if guess not in word:
 
        turns -= 1

        #alle falschen buchstaben werden in die liste eingetragen
        falschebuchstaben += guess
 
        
        os.system("clear")
        print("Falsch")
        print("bisher verwendet: ", falschebuchstaben)
        print("\n") 

 
        