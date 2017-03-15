import random
import sys
import time


class Load:
    def file(name):
        with open(name+".txt", "r") as f:
            return f.read()

    def life(num):
        with open("life" + str(num) + ".txt", "r") as f:
            return f.read()

    def capitals():
        with open("capitals.txt", "r") as file1:
            return file1.read().splitlines()


class Game:
    def random_capital_number(metropolies):
        return random.randint(1, len(metropolies))

    def greeting(encrypted, answer, essentiality):
        print ("\n"*5)
        print(Load.file("welcome"))
        print ("        ***WELCOME TO EVIL SKYNET! Hahahahaha***") # Intro
        print ()
        time.sleep(3)
        print ()
        print ("         Today I'll destroy one European capital!")
        print ("               GUESS which or DIE!!!")
        time.sleep(1)
        print ("       Hahahahahahahahahahahahahahahahahahahahahaha")
        time.sleep(1)
        print ("\n"*2)
        print ("                    <?>",encrypted,"<?>")
        print ()
        # print ("                                                TEST: ", answer) # correct answer, only for test.
        print(Load.life(essentiality))
        print ("Your life:", essentiality)

    def all_word(answer, essentiality):
        all_word = input("What is the answer? ")
        all_word = all_word.upper()

        if all_word != answer:
            print ("WRONG!!!")
            essentiality = essentiality - 2
            if essentiality < 0:
                essentiality = 0
            print(Load.life(essentiality))
            print("Your life:", essentiality)
        elif all_word == answer:
            answer = all_word
            return False

    def letter(answer, marker, essentiality, used_letters):
        guess = input("Choose a letter: ")
        guess = guess.upper()

        if guess in answer and len(guess) < 2: # If letter is correct
            return Game.correct_letter(answer, marker, guess, essentiality)

        elif guess not in answer or guess > 2: # If letter is incorrect
            Game.incorrect_letter(guess, essentiality, used_letters)
            return marker, essentiality-1

    def correct_letter(correct_answer, marker, guess, essentiality):
        time.sleep(1)
        print ("YESSS my presious!", guess, "is correct.")
        print()
        marker_list = list(marker)

        for i in range(len(correct_answer)):
            if guess == correct_answer[i]:
                marker_list[i] = guess

        marker = ''.join(marker_list)
        print ("                    <?>", marker, "<?>")
        print("Your life:", essentiality)
        return marker, essentiality

    def incorrect_letter(guess, essentiality, used_letters):
        time.sleep(1)
        print ("Not this time!")
        print ()
        essentiality = essentiality - 1
        print (Load.life(essentiality))
        print("Your life:", essentiality)
        numbers = ("0,1,2,3,4,5,6,7,8,9")

        if len(guess) < 2 and guess not in used_letters and guess not in numbers: # Add wrong letter to used_letters list
            used_letters.append(guess)

    def win_game(answer, amount, start_time, steps):
        print ()
        print ("                           OH, NO! YOU WIN.")
        time.sleep(1)
        print ("                     YOU ARE SMARTER THAN YOU LOOK...")
        time.sleep(1)
        print ("                           YOU SAVED", answer)
        print (Load.file("win"))

        time_guess = (time.time() - start_time)
        time_guess = round(time_guess)
        name = input("What is your name? ")
        print ()
        print (name+",","you are a hero in", answer)
        print ("YOUR TIME: ", time_guess, "seconds")
        print ("YOUR STEPS:", steps)
        print ("Congratulations!!!")
        print ()

        Game.highscore(name, time_guess, amount, answer)

    def highscore(name, all_time, amount, answer):
        file1 = open("highscore.txt", "a") # Export highscores to file
        for el in name, all_time, amount, answer:
            file1.write(str(el)+"|")
        file1.write("\n")
        file1.close()

    def lose_game(answer):
        print ("\n"*2) # If you are dead
        print ("             GAME OVER! YOU ARE DEAD! HAHAHAHA")
        time.sleep(3)
        print ("                ", answer, "IS DESTROYED!!!")
        print (Load.file("lose"))

    def play_again():
        while True:
            again = input("Do you want to play again? yes/no ")
            if again == "yes":
                Main.game()
            elif again == "no":
                sys.exit()
            else:
                print ("I do not understand! Type again, please.")


class Main:
    def game():
        capitals = Load.capitals()
        used_letters = []
        scores = []
        life = 5
        steps = 0
        capital_number = Game.random_capital_number(capitals)
        word = (capitals[capital_number-1])
        word = word.upper()
        mark = "_" * len(word)
        start_time = time.time()

        Game.greeting(mark, word, life)

        while True:
            if life < 1:
                break

            if word == mark:
                break

            print ("Wrong letters:", used_letters)
            print ()
            l_or_w = input("letter(1) or word(2)?: ") # Letter or word

            if l_or_w == "2":
                steps += 1
                if Game.all_word(word, life) == False:
                    break
                else:
                    life = life - 2

            elif l_or_w == "1":
                steps += 1
                mark, life = Game.letter(word, mark, life, used_letters)

            elif l_or_w != "1" or l_or_w == "2":
                print ("I do not understand! Type it again.")

        if life > 0:
            Game.win_game(word, steps, start_time, steps)

        elif life < 1:
            Game.lose_game(word)

        Game.play_again()

Main.game()
