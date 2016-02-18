# @author David Daly 2016 VA, USA
# First Project in Python completed 2/16/2016 1-day build

import random
import time
import sys


score = [0,0,0]         # user_score, computer_score, number_of_draws
number_of_games = 10    # number of games in a round
current_game_number = 1 # current game in round
gamemode = 1            # 1 - first to "x" points wins  2 - best of "x" games. where x is number_of_games


def intro():
    print ""
    print ""
    print ""
    print ""
    print ""
    print ""
    print"--------------------------------------------------------------------------------"
    time.sleep(.1)
    print"--                    Welcome to Rock, Paper, Scisscors                       --"
    time.sleep(.1)
    print"--------------------------------------------------------------------------------"
    time.sleep(.1)
    print""
    print("for rules type rules() at any time or type help()")
    time.sleep(.1)
    print""
    time.sleep(.1)
    print""
    time.sleep(.1)
    print""
    time.sleep(.1)
    print""
    time.sleep(.1)
    print""
    time.sleep(.1)
    print""
    time.sleep(.1)
    print""
    time.sleep(.1)
    print""
    time.sleep(.1)
    print""
    time.sleep(.1)
    print""
    time.sleep(.1)
    print""
    time.sleep(.1)

def handle_menu_inputs(str):
    if str == "rules()" or str == "rule()" or str == "r()":
        rules()
        return 1
    elif str == "help()" or str == "h()":
        help()
        return 1
    elif str == "reset()" or str == "r()":
        reset_game()
        return 1
    elif str == "gamemode()" or str == "gm()":
        change_gamemode()
        return 1
    elif str == "number_of_games()" or str == "num_of_games()" or str == "number_of_game()" or str == "num_of_games()" or str == "num_of_game()" or str == "num_game()"or str == "num_g()" or str == "ng()":
        change_number_of_games()
        return 1
    elif str == "info()" or str == "i()":
        print_game_info()
        return 1
    elif str == "exit()" or str == "quit()":
        print "Good bye."
        sys.exit()
    else:
        return 0
def rules():
    print""
    time.sleep(.1)
    print "--------------------------"
    time.sleep(.1)
    print "-  Rock beats Scissors   -"
    time.sleep(.1)
    print "-  Scissors beats Paper  -"
    time.sleep(.1)
    print "-  Paper beats Rock      -"
    time.sleep(.1)
    print "--------------------------"
    time.sleep(.1)
    print ""
    time.sleep(.1)
    print""
    time.sleep(.1)
def help():
    print""
    time.sleep(.1)
    print "-------------------------- List of Functions ------------------------"
    time.sleep(.1)
    print "rules() - lists rules"
    time.sleep(.1)
    print "number_of_games() / ng() - changes the number of games"
    time.sleep(.1)
    print "gamemode() / gm()- changes gamemode"
    time.sleep(.1)
    print "help() - lists all functions"
    time.sleep(.1)
    print "reset() - resets score"
    time.sleep(.1)
    print "info() - get game information"
    time.sleep(.1)
    print "exit() - leave game"
    time.sleep(.1)
    print "---------------------------------------------------------------------"
    time.sleep(.1)
    print ""
    time.sleep(.1)
def change_gamemode():
    print "Set gamemode to 1 - first to %d points wins or 2 - best of %d games" % (number_of_games,number_of_games)
    user_choice = raw_input("This will reset your score: ")
    if user_choice == "1" or user_choice == "2":
        global gamemode
        gamemode = int(user_choice)
        reset_game()
        print_game_info()
    else:
        print "gamemode was not changed"
        handle_menu_inputs(user_choice)
def change_number_of_games():
    print "How many games would you like to play: (1 - 49)"
    user_choice = raw_input("This will reset your score: ")
    try:
        user_choice = int(user_choice)
        if user_choice > 0 and user_choice < 49:
            global number_of_games
            number_of_games = user_choice
            print "number of games was set to %d" % number_of_games
            reset_game()
    except Exception as StringToIntError:
        if cancel_function(user_choice) or handle_menu_inputs(user_choice):
            pass
        else:
            print "please choose a number from 1-49 or type cancel"
            change_number_of_games()
def cancel_function(str):
    if str == "cancel" or str == "no" or str == "n" or str == "exit" or str == "stop" or str == "quit":
        return True
    else:
        return False
def get_computer_selection():
    comp_possible  = 0,1,2
    comp_choice = random.choice(comp_possible)
    print_computer_selection(comp_choice)
    return comp_choice
def print_computer_selection(comp_choice):
    if comp_choice == 0:
        print("the computer choice rock")
    elif comp_choice == 1:
        print("the computer choice scissors")
    elif comp_choice == 2:
        print("the computer choice paper")
def get_user_selection():
    user_choice = raw_input("Choose (R)ock, (P)aper, or (S)cissors: ")
    user_choice = user_choice.lower()
    if handle_menu_inputs(user_choice):
        return get_user_selection()
    elif user_choice == "r" or user_choice == "rock":
        return 0
    elif user_choice == "s" or user_choice == "scissors":
        return 1
    elif user_choice == "p" or user_choice == "paper":
        return 2
    else:
        print("That is not a vaild option.")
        return get_user_selection()
# @author David Daly 2016 VA, USA
def pick_winner(comp_choice, user_choice):
    # 0/rock     beats 1/scissors
    # 1/scissors beats 2/paper
    # 2/paper    beats 0/rock
    if user_choice == comp_choice:
        print("it's a draw!")
        update_score(2)
    elif user_choice == (comp_choice+1)%3:
        print("You won!")
        update_score(0)
    else:
        print("Computer wins")
        update_score(1)
def update_score(winner):
    # user_score, computer_score, number_of_draws
    if winner == 0 or winner == 1 or winner == 2:
        score[winner] += 1
    else:
        print("ERROR -- invaild score id")
def print_score():
    global score
    print ""
    time.sleep(.1)
    print "-------------------------------------"
    time.sleep(.1)
    print "   You: %d Computer: %d Draws: %d" % (score[0], score[1], score[2])
    time.sleep(.1)
    print "-------------------------------------"
    time.sleep(.1)
    print ""
    time.sleep(.1)
def print_gamemode():
    global gamemode
    if gamemode == 1:
        time.sleep(.1)
        print "you are playing in gamemode 1 - first to %d points wins" % number_of_games
    elif gamemode == 2:
        time.sleep(.1)
        print "you are playing in gamemode 2 - best of %d games" % number_of_games
def reset_game():
    global score
    global current_game_number
    score = [0,0,0]
    current_game_number = 1
    print "Your game has been reset."
    print_game_info()
def play_again():
    user_choice = raw_input("Would you like to play again?: (y/n) ")
    user_choice = user_choice.lower()
    if user_choice == "y" or user_choice == "yes" or user_choice == "y " or user_choice == "yes ":
        reset_game()
        game_controller()
        return 1
        # @author David Daly 2016 VA, USA
    elif user_choice == "n" or user_choice == "no" or user_choice == "n " or user_choice == "no ":
        # end game
        print""
        time.sleep(.1)
        print"--------------------------------------------------------------------------------"
        time.sleep(.1)
        print"--------------------------------------------------------------------------------"
        time.sleep(.1)
        print"--------------------------------------------------------------------------------"
        time.sleep(.1)
        print"--- Thank --------------------------- Rock, ------------------------------------"
        time.sleep(.1)
        print"-------- you ----------------------------- Paper, ------------------------------"
        time.sleep(.1)
        print"------------ for ------------------------------ Scissors! ----------------------"
        time.sleep(.1)
        print"---------------- playing--------------------------------------------------------"
        time.sleep(.1)
        print"--------------------------------------------------------------------------------"
        time.sleep(.1)
        print"----------------------- Made by David Daly 2016 VA -----------------------------"
        time.sleep(.1)
        print"--------------------------------------------------------------------------------"
        time.sleep(.1)
        print"--------------------------------------------------------------------------------"
        time.sleep(.1)
        print"--------------------------------------------------------------------------------"
        time.sleep(.15)
        print ""

        return 0
    else:
        print("that is an invaild choice")
        play_again()
def play_round():
    user_choice = get_user_selection()
    comp_choice = get_computer_selection()
    pick_winner(user_choice,comp_choice)
def declare_winner():
    global score
    declare_winner_hype()
    print ""
    if score[0] == score[1]:
        print "it's a tie!"
    elif score[0] > score[1]:
        print "you won!"
    else:
        print "you lost. better luck next time."
    print_game_info()

def declare_winner_hype():
    print "and the winner is ....."
    time.sleep(.5)
    print "."
    time.sleep(.5)
    print "."
    time.sleep(.5)
    print "."
    time.sleep(.5)
    print "."
    time.sleep(.5)
    print "."
    time.sleep(.5)
def print_game_info():
    print_gamemode()
    print_score()
def check_win_condition():
    global gamemode
    if gamemode == 1: # first to "x" wins
        if score[0] == number_of_games or score[1] == number_of_games:
            declare_winner()
            return True
        else:
            return False
    elif gamemode == 2: # best of "x" games
        if current_game_number > number_of_games:
            declare_winner()
            return True
        else:
            return False
    else:
        return False
# @author David Daly 2016 VA, USA
def game_controller():
    global current_game_number
    while not check_win_condition():
        play_round()
        current_game_number += 1
        if current_game_number%5 == 1:
            print_game_info()
    play_again()

intro()
print_game_info()
game_controller()
