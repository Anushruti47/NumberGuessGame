import random

def getRandomNumber():
    return random.randrange(1,100)

def getHint(number,guess):
    if guess > number+10 or guess < number-10:
        return "Cold"
    elif guess == number:
        return "Right"
    else:
        return "Hot"


def runguess():
    secret_number=getRandomNumber()
    while True:
        user_guess=int(input("Enter a number between 1 and 100:"))
        hint=getHint(secret_number,user_guess)
        if hint=="Right":
            print("You guessed it right!")
            break
        else:
            print(hint)

if __name__ == '__main__':
    runguess()
