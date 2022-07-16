#1 /usr/bin/python3

import random

print('Welcome to Rock, Paper, Scissors!')

options = ['rock', 'paper', 'scissors']

myChoice = input('Choose your option: ').lower()
computerSelect = random.choice(options)
print(f'The computer chose: {computerSelect}')

win = 'You win!'

if myChoice == 'rock' and computerSelect == 'scissors':
    print(win)
else: ('you lose')

elif myChoice == 'paper' and computerSelect == 'rock':
    print(win)
else: ('you lose')

elif myChoice == 'scissors' and computerSelect == 'paper':
    print(win)
else: ('you lose')

  



