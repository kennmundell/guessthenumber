# Guess the number # by Kenneth Mundell
import random
import os

from art import logo
os.system('cls')
print(logo)
#no_of_plays = 10
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0

answer = random.randint(1,100)

# Function to check if the user is correct
def check_answer(guess, answer, turns):

    """ checks answer against turns. Return the number of turns remaining """
    if guess > answer:
        print("Too high. Guess again")
        return turns -1
    elif guess < answer:
        print("Too low. Guess again!")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}")

# Set difficulty
def set_difficulty():
    level = input("Choose a difficulty. 'easy' or 'hard' ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to my number guessing game!")
    print("Please guess a number between 1 and 100 and i will tell you how close you are ")
    turns = set_difficulty()



    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining")

    #correct = random.randint(1,100)
    #p#rint(correct)
    #game = True


    #level = input("Type 'h' for hard for 5 plays or 'e' for 10 plays: ")

        guess = int(input("Make a guess "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of goes. You lose.")
            return
        elif guess != answer:
            print("Guess again")
            print()

game()
