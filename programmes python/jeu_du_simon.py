import time
import random
import os

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')


def ask_sequence(nb_character):
    the_sequence = ""
    for i in range(nb_character):
        character = random.randint(0, 9)
        the_sequence += str(character)
    return the_sequence





print("----- Gamme of Simon -----")
print("memorize the following sequence")


print("1- easy")
print("2- normal")
print("3- hard")

level = input("select the level : ")
if level == "1":
    number_of_characters = 2
    pause = 5

elif level == "2":
    number_of_characters = 3
    pause = 4

elif level == "3":
    number_of_characters = 4
    pause = 3

clear_screen()
print("Are you ready? ok lets start")
time.sleep(3)
clear_screen()

print("memorize the following sequence")
sequence = ask_sequence(number_of_characters)


life = 3
while life > 0:
    print(sequence)
    time.sleep(3)
    clear_screen()
    answer = input("now enter the last sequence : ")

    if answer == sequence:
        print("good")
        time.sleep(2)
        clear_screen()
        print("New sequence")
        new_character = random.randint(0, 9)
        sequence += str(new_character)


    else:
        print("bad... Try again")
        life -=1
        time.sleep(2)
        clear_screen()

print("You lost. you will do better next time")

