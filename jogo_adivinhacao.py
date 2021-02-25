import random

guess = 1

print('I will thin of a number between 1 and 10 and you shoul guess it.')
picked_number = random.randint(1, 10)
while guess != picked_number:
    guess = int(input('Guess what number I just picked? '))
print('Congrats, you just guessed my number!')


# teste