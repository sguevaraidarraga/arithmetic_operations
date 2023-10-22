from operations import *

def game():
    score = 0
    while True:
        print('======== Menu ========'
              '\n1. Addition'
              '\n2. Subtraction'
              '\n3. Multiplication'
              '\n4. Division'
              '\n5. Power'
              '\n6. Modulo'
              '\n0. Exit')
        option = int(input('\nChoice an option: '))

        num_1 = input('Enter first number: ')
        num_2 = input('Enter second number: ')
        answer = int(input('Enter you answer: '))

        if option == 1:
            result = addition(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
        elif option == 2:
            result = subtraction(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
        elif option == 3:
            result = multiplication(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
        elif option == 4:
            result = division(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
        elif option == 5:
            result = power(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
        elif option == 1:
            result = modulo(num_1, num_2)
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