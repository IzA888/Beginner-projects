import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Advinhe um número entre 1 e {x}: '))
        if guess < random_number:
            print('Tente de novo. Muito baixo')
        elif guess > random_number:
            print('Tente de novo. Muito alto')


    print(f'EBA! Parabéns, Você acertou o número {random_number}!')

guess(10)