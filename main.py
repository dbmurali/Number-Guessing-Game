from numbers import Number
from random import random
import random
from tkinter.constants import PROJECTING

from art import logo
from art import GAME_OVER
from art import heart
print(logo)

to_play=True
while to_play:
    def game():
        level=input().lower()
        OG_NUMBER=random.randrange(1,100)

        if level=="easy":
            print("You selected easy level")
            life=10
        else:
            print("You selected hard level")
            life=5

        for point in range(1,life+1):
            rem_life=life-point
            user_guess=int(input("guess the number"))
            if user_guess==OG_NUMBER:
                print("You guessed correctly")

            elif user_guess>OG_NUMBER:
                print("Guessed number too high")
                print(f"Wrong Gues, remaining life>>  {heart*rem_life} ")
            elif user_guess<OG_NUMBER:
                print("Guessed number too low")
                print(f"Wrong Guess, remaining life>>  {heart*rem_life} ")

        print(" Out of life 💔")


        restart = input("Press \"E\" for play again and \"C\" for end").lower()
        if restart == "e":
            game()
        else:
            print(GAME_OVER)


    game()

