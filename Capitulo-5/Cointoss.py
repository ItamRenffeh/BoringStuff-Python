import random

guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().strip().lower()

toss = random.choice(('heads', 'tails'))

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')

    guess = input().strip().lower()

    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')