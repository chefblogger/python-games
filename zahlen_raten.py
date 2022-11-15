import os
import random

os.system('clear')


gesuchte_zahl = random.randint(1,10)

rate = int(input("deine zahl: "))

while gesuchte_zahl != rate:

    if rate < gesuchte_zahl:
        print("+++ zu niedrig +++")
        rate = int(input("deine zahl: "))

    elif rate > gesuchte_zahl:
        print("--- zu hoch ---")
        rate = int(input("deine zahl: "))
    else:
        break

print ("=== korrekt ===")
