from operations import *

def game():
    score = 0
    while True:
        print('======== Menu ========'
              '\n2. Subtraction'
              '\n0. Exit')
        option = int(input('\nChoice an option: '))

        num_1 = input('Enter first number: ')
        num_2 = input('Enter second number: ')
        answer = int(input('Enter you answer: '))

        if option == 2:
            result = subtraction(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
        else:
            break

        print(f'======== Game Over ========'
        f'\nYou score is {score}'
        '\nKeep going!')

game()
