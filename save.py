import random

guessesTaken = 0
number = 556

print ("Привет, как тебя зовут?")
myName = input()
print ("Ну что, %s , готов?", myName)

myNumber = random.randint(1, 10)



while (guessesTaken < 6):
    print ("Напиши свой вариант загаданного числа: ")
    guess = int(input())
    guessesTaken = guessesTaken + 1

    if (guess < myNumber):
        print ("Ваше число меньше выбранного")


    if (guess > myNumber):
        print ("Ваше число больше выбранного")


    if (guess == myNumber):
        print ("Поздравляю, вы выиграли!")
        break
