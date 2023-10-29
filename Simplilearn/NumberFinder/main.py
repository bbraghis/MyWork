import random


def number_finder():
    num = random.randint(1, 9)
    guess = None
    while guess != num:
        guess = input('Guess a number between 1 and 9: ')
        guess = int(guess)
        if guess == num:
            print('Well guessed!')
        else:
            print('Nope, try again!')


if __name__ == '__main__':
    number_finder()
