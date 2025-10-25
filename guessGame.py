import random

def getSecretNumber():
    return random.randrange(1,100)

def getHint(number,guess):
    if guess > number+10 or guess < number-10:
        return "Cold"
    elif guess == number:
        return "Right"
    else:
        return "Hot"

def runguess():
    secretNumber=getSecretNumber()
    while True:
        guessNumber=int(input("Enter a number between 1 and 100: "))
        hint=getHint(secretNumber,guessNumber)
        if hint == "Right":
            print("You guessed it right!")
            break
        else:
            print(hint)

if __name__ == '__main__':
    runguess()