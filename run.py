# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import colorama
from colorama import Fore
from art import *
import sys
import time
colorama.init(autoreset=True)


def typewriter(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)


def validate_input(actual, accepted, decision):
    """
    Validates user input using accepted criteria
    """
    cont = True
    choice = actual
    print(choice)
    while cont:
        if choice in accepted:
            cont = False
        else:
            print(f"Invalid input: Input must be one of the following inputs: {accepted}")
            choice = input(f"{decision}")
    return choice


def start_game():
    """
    Initialise a new game
    """
    # print(f"{Fore.Green}{opening_logo}")
    print(f"{Fore.YELLOW}{opening_logo}")
    typewriter('Welcome!\n')
    typewriter('You are about to take on the role of Guybrush Threepwood\n')
    typewriter('The villainous ghost pirate LeChuck has kidnapped Governor Elaine Marley\n')
    typewriter('You have procured your own pirate ship and assembled a crew\n')
    typewriter('You must now pursue LeChuck back to his hideout on Monkey Island\n')
    user_state = input("Are you ready to begin the adventure: Y/N \n").lower()
    valid = validate_input(user_state, ['y', 'n'], "Are you ready to begin the adventure: Y/N \n")
    return valid


def game_over():
    """
    Displays Game Over screen and gives choice to restart
    """
    print(f"{Fore.RED}{gameover}")
    typewriter('Well I guess Elaine can fend for herself and LeChuck wins\n')
    typewriter('Some pirate you turned out to be...\n')
    user_state = input("Would you like to try again: Y/N \n").lower()
    valid = validate_input(user_state, ['y', 'n'], "Would you like to try again: Y/N \n")
    return valid


def goodbye():
    """
    displays Goodbye screen if the player chooses not to try again following Game Over
    """
    print(f"{Fore.CYAN}{exit_message}")
    typewriter('Thank you for playing, I hope you enjoyed the adventure\n')
    typewriter('Come back and try again soon\n')


def ship_deck():
    """
    First game choice; sets the scene for the player and gives options about how to proceed
    """
    print(f"{Fore.YELLOW}{pirate_ship}")
    typewriter('You have set sail with your crew and are stood aboard the deck of your ship The Sea Monkey\n')
    typewriter('Your crew have decided this is more of a leisurely cruise rather than a rescue mission\n')
    typewriter('You will need to brew the magic potion enabling travel to Monkey Island yourself\n')
    typewriter('Explore the ship and find a "Jolly Roger Flag", "Cinnamon Stick", "Gunpowder", "Fine Wine" and "Ink"\n')
    typewriter('Items will be added to your inventory automatically as you find them\n')
    typewriter('Use the "Required" command at any input to see what\'s left to find\n')
    typewriter('You are on the deck, before you is the ladder to the crow\'s nest, a door to the captain\'s cabin')
    typewriter('Or stairs leading below deck, the choice is yours')
    user_state = input("Where would you like to go? : LADDER/DOOR/STAIRS\n").lower()


def main():
    valid = start_game()
    if valid == 'y':
        print('next choice')
    elif valid == 'n':
        valid = game_over()
        if valid == 'y':
            valid = start_game()
        elif valid == 'n':
            goodbye()
    else:
        print("Unforeseen Error: Please Restart")


main()
