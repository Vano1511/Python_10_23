from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
NUMBER_OF_TRIES = 10

guessing_number = randint(LOWER_LIMIT, UPPER_LIMIT)
tries = 1
while tries <= NUMBER_OF_TRIES:
    while True:
        try:
            input_try = int(input(f"try № {tries} of {NUMBER_OF_TRIES}."
                                  f"\nEnter digit between {LOWER_LIMIT} and {UPPER_LIMIT}: > "))
            break
        except ValueError:
            print("You input not a digit")
    if input_try == guessing_number:
        print("Wright! You are guess my number! You win!")
        exit()
    elif input_try > guessing_number:
        print("my number is LOWER than yours")
    else:
        print("my number is HIGHER than yours")
    tries += 1
print("The attempts are over. You lose")
