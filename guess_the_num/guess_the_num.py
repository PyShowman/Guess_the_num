# "Guess_the_num" game
import random

print('Select the range of nums')
num = random.randint(int(input('From:')), int(input('To:')))
att = int(input('Select attempts:'))
ug = str(num)
def func(x):
    for i in range(len(ug)):
        if i < len(x) and x[i] == ug[i]:
            print(f'The {i + 1}-th digit is right!')
while att <= 0:
    print('Sorry, choose another number!')
    att = int(input('Select attempts:'))
else:
    print(f'Welcome to "Guess_the_num game" now u had {att} attempts to find a secret number.\nI made up a {len(str(num))}-digit number\nGood luck!')
    for i in range(att):
        a = input(f'Guess the {len(str(num))}-digit number:')
        if not a.isdigit() or len(a) != len(ug):
            print('Enter a valid number with the correct number of digits!')
            continue
        if int(a) == num:
            print(f"Wow! There's a winner!Nice try. What about play again?\nYour num was {num}")
            break
        func(a)
    else:
        print(f'Sorry, but u lose. Try again later!\nYour num was {num}')