from random import randrange

# "CONSTANTS"
NO_DIGITS = 4
SEP = "=" * 32


# Generate secret number for the game
def generateSecret():
    secret = ""
    for _ in range(NO_DIGITS):
        while True:
            r = str(randrange(0, 9))
            alreadyExists = False
            for c in secret:
                if c == r:
                    alreadyExists = True
                    break
            if alreadyExists: continue
            secret += r
            break
    return secret


# Verify in secret number is ok (ciphers may not repeat)
def isValidGuess(guess):
    # invalid length
    if len(guess) != NO_DIGITS: return False
    # Check that characters are valid ciphers and calculate their frequency
    frequencies = {}
    for c in str(guess):
        if c < '0' or c > '9': return False
        frequencies[c] = frequencies.get(c, 0) + 1
    # Check that every cipher occurs only
    for c, f in frequencies.items():
        if f > 1: return False
    return True


def calculateBulls(guess, secret):
    if len(guess) != len(secret): return -1
    bulls = 0
    for i in range(0, len(guess)):
        if (guess[i] == secret[i]): bulls += 1
    return bulls


def calculateCows(guess, secret):
    if len(guess) != len(secret): return -1
    cows = 0
    for i in range(0, len(guess)):
        c = guess[i]
        for j in range(0, len(secret)):
            if (j == i): continue
            if (secret[j] == c):
                cows += 1
                break
    return cows


print(SEP)

################
# BULLS & COWS #
################
print(f"""Welcome to the Bulls & Cows game. 
Let's go playing, enjoy it!""")

print(SEP)

# Generate the secret number
secretNumber = generateSecret()
print(f'My secret number is {secretNumber}. Don\'t tell anybody.')

print(SEP)

# Loop until the users guesses the corret number
numberOfGuesses = 0
while True:
    guess = input("Enter you guess: ")
    # Invalid guess - promt the user to enter another guess
    if not (isValidGuess(guess)):
        print("Invalid guess. Please try again.")
        continue
    numberOfGuesses += 1
    # Break the loop if secret number found
    if guess == secretNumber: break
    bulls = calculateBulls(guess, secretNumber)
    cows = calculateCows(guess, secretNumber)
    print(f'Bulls={bulls} & Cows={cows}')

print(SEP)

print(f'Finished after {numberOfGuesses} attempt(s).')

print(SEP)

# Read the welcome screen from file and print it
print(f"""!!! Congratulations !!!""")
print(f"""You have just guessed the secret number!
Thanks for playing, hope to see you soon again!""")