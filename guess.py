import random
import sys
import timeit

if len(sys.argv) <=1:
    z=30
else:
    z=int(sys.argv[1])

number=int(random.randint(1,z))

print ("Welcome in ***Guess the Number*** game!")
name = input ("What's your name? ")
print ("Well,",name+",","I am thinking of a number between 1 and 30.")
tries=1

while True:
    guess = input("What is your guess? ")

    try:
        if int(guess) == number:
            print ("YES!!!",number,"is my secret number! You guessed my number in", tries, "guesses. Congratulations!!!")
            print ()
            input("Press any key to exit program")
            break
        elif int(guess) < number:
            print (guess, "is too low")
        elif int(guess) > number:
            print (guess, "is too high")
    except:
        print ("Please again!")
    tries+=1
