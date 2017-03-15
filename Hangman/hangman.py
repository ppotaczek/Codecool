def game():
    import random,sys,time
    capitals=[]
    used_letters=[]
    scores=[]
    l=0
    with open("stolice.txt", "r") as file1: # Import capitals
        capitals=file1.read().splitlines()

    random_capital=(random.randint(1,len(capitals))) # Pick random capital
    word=(capitals[random_capital-1])
    word=word.upper()
    mark="_"*len(word)
    life = (
    """
    _______
    ||    |
    ||
    ||
    ||
    ||
    ||
    ||
    ||
_5__||________
    """,
    """
    _______
    ||    |
    ||    O
    ||
    ||
    ||
    ||
    ||
    ||
_4__||_________
    """,
    """
    _______
    ||    |
    ||    O
    ||  --+--
    ||
    ||
    ||
    ||
    ||
_3__||_________
    """,
    """
    _______
    ||    |
    ||    O
    ||  /-+-\\
    || /  |  \\
    ||
    ||
    ||
    ||
_2__||_________
    """,
    """
    _______
    ||    |
    ||    O
    ||  /-+-\\
    || /  |  \\
    ||   / \\
    ||  /   \\
    ||
    ||
_1__||_________
    """
    ,
    """
    _______
    ||    |
    ||    @
    ||  /-+-\\
    || |  |  |
    ||   / \\
    ||  |   |
    ||
    ||
_0__||_________
    """
    ,
    """
    _______
    ||    |
    ||    @
    ||  /-+-\\
    || |  |  |
    ||   / \
    ||  |   |
    ||
    ||
_0__||_________
    """)
    print ("\n"*5)
    print('''
          _==/           i     i           \==_
         /XX/            |\___/|            \XX\\
       /XXXX\            | 0,0 |            /XXXX\\
      |XXXXXX\_         _| --- |_         _/XXXXXX|
     XXXXXXXXXXXxxxxxxxXXX     XXXxxxxxxxXXXXXXXXXXX
    |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
     XXXXXX/^^^^"\XXXXXXXXXXXXXXXXXXXXX/^^^^^\XXXXXX
      |XXX|       \XXX/^^\XXXXX/^^\XXX/       |XXX|
        \XX\       \X/    \XXX/    \X/       /XX/
           "\       "      \X/      "       /"
    ''')
    print ("        ***WELCOME TO EVIL SKYNET! Hahahahaha***") # Intro
    print ()
    time.sleep(3)
    print ()
    print ("         Today I'll destroy one European capital!")
    print ("               GUESS which or DIE!!!")
    time.sleep(1)
    print ("       Hahahahahahahahahahahahahahahahahahahahahaha")
    time.sleep(1)
    start_time = time.time() # start time
    steps=0                  # start steps
    print ("\n"*2)
    print ("                    <?>",mark,"<?>")
    print ()
    print ("                                                TEST: ",word) # correct answer, only for test.
    print ("Your life:", life[l])


    while l<5: # If you are not dead
        while mark!=word: # If you didn't win yet
            if l>=5:
                break
            print ("Wrong letters:", used_letters)
            print ()
            letter_or_word=input("letter(1) or word(2)?: ")

            if letter_or_word=="2": # Add word
                all_word=input("What is the answer? ")
                all_word=all_word.upper()
                steps+=1
                if all_word!=word:
                    print ("WRONG!!!")
                    l=l+2
                    print("Your life:", life[l])
                else:
                    word=all_word
                    break
            elif letter_or_word=="1": # Add letter
                guess=input("Choose a letter: ")
                guess=guess.upper()
                new_mark=""
                steps+=1
                if guess in word and len(guess)<2: # If letter is correct
                    time.sleep(1)
                    print ("YESSS my presious!", guess, "is correct.")
                    print()
                    for i in range(len(word)):
                        if guess==word[i]:
                            new_mark+=guess
                        else:
                            new_mark+=mark[i]
                    mark=new_mark
                    print ("                    <?>",new_mark,"<?>")
                    print("Your life:", life[l])
                elif guess not in word or guess>2: # If letter is incorrect
                    time.sleep(1)
                    print ("Not this time!")
                    print ()
                    print ("                    <?>",mark,"<?>")
                    print()
                    l=l+1
                    print("Your life:", life[l])
                    numbers=("0,1,2,3,4,5,6,7,8,9")
                    if len(guess)<2 and guess not in used_letters and guess not in numbers: # Add wrong letter to used_letters list
                        used_letters.append(guess)
            elif letter_or_word!="1" or letter_or_word=="2":
                print ("I do not understand! Type it again.")

        if l<5:
            print ()
            print ("                           OH, NO! YOU WIN.")
            time.sleep(1)
            print ("                     YOU ARE SMARTER THAN YOU LOOK...")
            time.sleep(1)
            print ("                           YOU SAVED", word)
            print ('''
                  _==/          __     __          \==_
                 /XX/            |\___/|            \XX\\
               /XXXX\            | 0,0 |            /XXXX\\
              |XXXXXX\_         _|  O  |_         _/XXXXXX|
             XXXXXXXXXXXxxxxxxxXXX     XXXxxxxxxxXXXXXXXXXXX
            |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            |XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
             XXXXXX/^^^^"\XXXXXXXXXXXXXXXXXXXXX/^^^^^\XXXXXX
              |XXX|       \XXX/^^\XXXXX/^^\XXX/       |XXX|
                \XX\       \X/    \XXX/    \X/       /XX/
                   "\       "      \X/      "       /"
            ''')

            time_guess = (time.time() - start_time)
            time_guess = round(time_guess)
            name=input("What is your name? ")
            print ()
            print (name+",","you are a hero in", word)
            print ("YOUR TIME: ", time_guess, "seconds")
            print ("YOUR STEPS:", steps)
            print ("Congratulations!!!")
            print ()

            file1=open("highscore.txt", "a") # Export highscores to file
            for el in name, time_guess, steps, word:
                file1.write(str(el)+"|")
            file1.write("\n")
            file1.close()

            while True: # One more time?
                again=input("Do you want to play again? yes/no ")
                if again=="yes":
                    game()
                elif again=="no":
                    sys.exit()
                else:
                    print ("I do not understand! AGAIN!!!")

    print ("\n"*2) # If you are dead
    print ("             GAME OVER! YOU ARE DEAD! HAHAHAHA")
    print ("Your life:", life[l])
    time.sleep(3)
    print ("                ",word,"IS DESTROYED!!!")
    print ('''
            )           )        (                   )
          (                       )      )            .---.
      )              (     .-""-.       (        (   /     \\
     ( .-""-.  (      )   / _  _ \        )       )  |() ()|
      / _  _ \   )        |(_\/_)|  .---.   (        (_ 0 _)
      |(_)(_)|  ( .---.   (_ /\ _) /     \    .-""-.  |xxx|
      (_ /\ _)   /     \   |v==v|  |<\ />|   / _  _ \ '---'
       |wwww|    |(\ /)|(  '-..-'  (_ A _)   |/_)(_\|
       '-..-'    (_ o _)  )  .---.  |===|    (_ /\ _)
                  |===|  (  /     \ '---'     |mmmm|
                  '---'     |{\ /}|           '-..-'
                            (_ V _)
                             |"""|
                             '---'
    ''')

    while True:
        again=input("Do you want to play again? yes/no ")
        if again=="yes":
            game()
        elif again=="no":
            sys.exit()
        else:
            print ("I do not understand! Type again, please.")

game()
