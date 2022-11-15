import os
import random

os.system('clear')

words = ['welt', 'baum', 'erde', 'feuer']

word = random.choice(words)


random_wort = random.sample(word, len(word))
gemixt_wort = ''.join(random_wort)

#print("gewähltes wort: ", word)
print("vermischt: ", gemixt_wort)

geraten = input("Wie lautet das Wort? ")

while word != geraten:
    if word != geraten:
        print("--- FALSCH ---")
        os.system('clear')
        print("vermischt: ", gemixt_wort)
        geraten = input("Wie lautet das Wort? ")

    elif word == geraten:
        print("KORREKT")
    else:
        break

print("=== KORREKT ===")