import random

def hangman():
    print('\nWelcome to the HangMan game')

    fruits_list = ['apple', 'banana', 'grapes', 'kiwi', 'lime']
    secret = random.choice(fruits_list)
    hint = 'aeoi'
    turns = 5

    while turns > 0:
        missed = 0
        for check in secret:
            if check in hint:
                print(check, end = ' ')
            else:
                print('_', end = ' ')
                missed += 1

        if missed == 0:
            print('\n\nYou win!')
            break

        guess = input('\n\nName the Letter: ')
        hint += guess

        if guess not in secret:
            turns -= 1
            print("\nDidn't guess")
            print('\nThere are still attempts Left: ', turns)
            if turns < 5: print('\n__', '\n  |  ')
            if turns < 4: print('  o  ')
            if turns < 3: print(' /|\  ')
            if turns < 2: print('  |  ')
            if turns < 1: print(' / \ ')
            if turns == 0: print('\nThe hidden word: ', secret)
answer = 'yes'

while answer == 'yes':
    hangman()
    print('\nDo you want to play again? input: yes or no')
    answer = input()


