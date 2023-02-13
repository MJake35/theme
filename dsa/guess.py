import random
guesses = []
number = random.randint(1, 100)


def guess():
    while True:
        guess = int(input("what number am I thinking of: "))
        guesses.append(guess)

        if guess == number:
            print(f"I was thinking of {number}")
            print(f"you guessed, {guess}")
            print(f"you have guessed the number in {len(guesses)}")
            break
        elif guess < number:
            print("guess higher")
        else:
            print("guess lower")


guess()