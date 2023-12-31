import random

secret = random.randint(1, 99)
guess = 0
tries = 0
print("AHOY! I'm the Dread Pirate Roberts, and I have a secret!")
print("It is a number from 1 to 99. I'll give you 6 tries. ")

while guess != secret and tries < 6:
    tries = tries + 1
    # debug1: add try except
    # debug2: move setting tries value on top of loop
    try:
        guess = int(input("What's yer guess? "))
    except ValueError:
        print("Please enter an integer")
        continue

    if guess < secret:
        print("Too low, ye scurvy dog!")
    elif guess > secret:
        print("Too high, landlubber!")

if guess == secret:
    print("Avast! Ye got it!  Found my secret, ye did!")
else:
    print("No more guesses!  Better luck next time, matey!")
    print("The secret number was", secret)
