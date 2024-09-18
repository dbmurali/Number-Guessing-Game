from tabnanny import check

from art import logo
from art import HEART
from art import WIN
from art import GAME_OVER
import random

def set_level(user):
    if user=="e":
        return 10
    else:
        return 5
def check_answer(guess,og_number,life):
    if guess>og_number:
        print("too high")
        return life-1
    elif guess<og_number:
        print("too low")
        return life-1
    else:
        return 20


def restart():
    game()
def game():
    print(logo)
    og_number=random.randint(1,100)
    user=input("print E for easy and H for Hard: ").lower()
    life=set_level(user)
    while life>0:
        try:
            guess=int(input("enter the number you guess: "))
            life=check_answer(guess,og_number,life)
            if life<=10:
             print(f"life remaining : {life*HEART} ")
            elif life==20:
                print(WIN)
                life=-1
        except ValueError:
            print("The value you typed is incorrect. Numerical values are the only ones accepted.")
         
    print(GAME_OVER)

    redo=input("enter y for re start start or N for end").lower()
    if redo=="y":
        print("\n"*100)
        restart()





game()
def win():
    print(WIN)
