import random
import os

a = ["home", "euphoria", "tendentious", "ram", "silo", "mango", "ranger", "wind", "slime", "happiness", "tuber", "forest", "spam"]

answer = list(random.choice(a))
bad_guesses = []
executioner = {1 : "head", 2 : "torso", 3 : "left leg", 4 : "right leg", 5 : "left arm" , 6 : "right arm (one left)", 7 : "bow tie"}
placeholder = ["-" for i in range(len(answer))]
count = 0

print "Let's play hangman!"

while count < 7:
    guess = raw_input("Guess a letter: ")
    for i in range(len(answer)):
        if guess == answer[i]: 
            placeholder[i] = answer[i]

    if guess in answer: 
        print "Got one! \n", ''.join(placeholder), "\nBad guesses:", ''.join(bad_guesses)
            
    elif guess not in answer:
        count += 1
        bad_guesses += guess
        print "One step closer to the grave", executioner[count], "\n", ''.join(placeholder),
        "\nbad guesses:", ''.join(bad_guesses) 
           
    if placeholder == answer:
        print "You win"
        again = raw_input("would you like to play again (y/n):")
        if again == "y":
            count = 0
        else: 
            break
    #os.system('clear')
