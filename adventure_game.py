# -*- coding: utf-8 -*-
import time
import random

def print_pause(message):
    print(message)
    time.sleep(1.5)

def intro(item , enemy):
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here, terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(f"In your hand you hold your trusty (but not very effective) {item}.")

def cave(inventory, score, color):
    if "Wand of Ogoroth" in inventory:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before. It's just an empty cave now.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It's small, but your eye catches a glint behind a rock.")
        print_pause("You have found the magical Wand of Ogoroth!")
        print_pause("You discard your rusty old magic wand and take the Wand of Ogoroth with you.")
        inventory.remove(f"rusty old {color} magic wand")
        inventory.append("Wand of Ogoroth")
        score += 1
    print_pause(f"Your score is now: {score}")
    return score

def house(inventory, enemy, score):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} finds you!")
    print_pause("Would you like to (1) cast a spell or (2) run away?")
    choice = input()
    if choice == "1":
        if "Wand of Ogoroth" in inventory:
            x = random.choice(["success", "failure"])
            if x == "success":
              print_pause(f"As the {enemy} moves to cast a spell, you raise your Wand of Ogoroth.")
              print_pause(f"You cast a spell on the {enemy}.")
              print_pause(f"The {enemy} is defeated!")
              score += 7
            else:
              print_pause(f"As the {enemy} moves to cast a spell, you raise your Wand of Ogoroth.")
              print_pause(f"The {enemy} sees your wand and runs away!")
              print_pause(f"You have rid the town of the {enemy} , but it could come back to defeat you")
              score += 3
        else:
            print_pause("You try to cast a spell, but your old wand fizzles.")
            print_pause("The enemy defeats you.")
            score -= 5
    elif choice == "2":
        print_pause("You run back to the field.")
        print_pause("Luckily, you weren't followed.")
        score -= 2
    else:
        print_pause("Invalid input. You hesitate and the enemy gets away.")
    print_pause(f"Your score is now: {score}")
    return score

def field(inventory, enemy, score, turns , color):
    while True:
        if score <= 0:
            print_pause("You've lost all your points. Your wand crumbles to dust.")
            print_pause("You have been defeated and must start again...")
            play_again()
            return
        if turns >= 6:
            print_pause("You have run out of time.")
            if score >= 10:
                print_pause("But your effort was enough to unlock the Final Challenge!")
                riddle_challenge()
            else:
                print_pause("You didn't gain enough points. Game over.")
                play_again()
                return
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        print_pause("What would you like to do?")
        choice = input("(Please enter 1 or 2.)\n")
        turns += 1
        if choice == "1":
            score = house(inventory, enemy, score)
        elif choice == "2":
            score = cave(inventory, score , color)
        else:
            print_pause("Invalid input.")
            continue

        if score >= 10:
            print_pause("You have reached 10 points! You now face the Final Challenge!")
            riddle_challenge()
            return

def riddle_challenge():
    print_pause("FINAL CHALLENGE: Answer this riddle to win the game.")
    print_pause("Riddle: How many months of the year have 28 days?")
    answer = input("Your answer: ").strip().lower()
    if "all" in answer or "12" in answer:
        print_pause("Correct! Every month has at least 28 days!")
        print_pause("You have won the game. Congratulations, hero!")
    else:
        print_pause("Wrong! The magic backfires and sends you home in shame.")
        print_pause("You lost the final challenge.")
    play_again()

def play_again():
    print_pause("Would you like to play again? (y/n)")
    choice = input().lower()
    if choice == "y":
        print_pause("Restarting the game ...")
        play_game()
    elif choice == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()

def play_game():
    color = random.choice(["blue", "yellow", "green" , "red"])
    inventory = [f"rusty old {color} magic wand"]
    enemy = random.choice(["wicked fairy", "troll", "dragon"])
    score = 5
    turns = 0
    intro(inventory[0],enemy)
    field(inventory, enemy, score, turns , color)

play_game()
