import random
import sys
name = input('What is your name:')

print("Hello " + str(name) + ". Good Luck!")

words = ['rainbow', 'cat', 'sun', 'duck', 'eyes', 'cheese', 'circle', 'egg', 'mouse', 'bridge', 'bone', 'grapes', 'bell', 'clock',
         'alligator', 'cloud', 'chicken', 'purse', 'moon', 'airplane', 'horse', 'pencil', 'lamp', 'coal', 'queen', 'electricity',
         'skate', 'deep', 'toast', 'nature', 'aircraft', 'bicycle', 'music', 'pirate', 'peach', 'pineapple', 'camera', 'brain',
         'shark', 'jungle', 'rubber', 'yolk', 'biscuit', 'dizzy', 'jazz', 'mirror', 'professor', 'download', 'vitamin',
         'avocado', 'world', 'sushi', 'dentist', 'drain', 'dream', 'gold', 'cliff', 'moth', 'sneeze', 'buffalo', 'leopard',
         'penguin', 'wolf', 'tiger', 'lion', 'frog']

word = []
word = random.choice(words)

turn = 10

guess = ''

while turn > 0:

    win = True

    for char in word:
        if char in guess:
            sys.stdout.write(char)

        else:
            sys.stdout.write('-')
            win = False

    if win == True:
        print('Congratulation, You Win***.')
        break

    i = str(input("Enter Character:"))
    if len(i) != 1:
        print('Please enter one exact character.')
        continue

    guess += i

    if i not in word:
        turn -= 1
        print('wrong, you have ', str(turn), ' turn')


if win == False:
    print('you lose')
