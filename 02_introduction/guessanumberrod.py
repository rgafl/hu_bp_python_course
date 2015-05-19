import random

Grenzen = (0, 100)
Versuche = 6

the_number = random.randint(*Grenzen)


print("Guess a number between 0 and 100")
print("You have 6 tries!")

for tries in range(Versuche):
    guess = int(input("Take a guess: "))

    if guess > the_number:
        print("Lower...")
    elif guess < the_number:
        print("Higher...")
    else:
        print("That's it! %d!" % (the_number))
        print("And it only took you %d tries!\n\n" % (tries + 1))
        break
else:
    print("You have no more tries left! :(")

# Admittedly a contorted way to write a statement that works in both Python 2 and 3...
try:
    input("Press the enter key to exit.")
except:
    pass
