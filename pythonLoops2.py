capitalGuess = input("What is the capital of Croatia? ").upper()
numberOfGuesses = 1

while capitalGuess != "ZAGREB":
    numberOfGuesses = numberOfGuesses + 1
    if numberOfGuesses > 3:
        print("You guessed incorrectly 3 times. Game Over")
        break
    capitalGuess = input("Guess again. ")

if numberOfGuesses <= 3:
    print("Correct! It took you " + str(numberOfGuesses) + " guesses")
