#Tic Tac Toe Unbeatable
#Anthony Swift
#03/04/2020

'''
A game of Tic Tac Toe that can be played against the computer or against another human player

Play against the computer:
Easy Mode - Computer chooses random positions on the board
Hard Mode - The computer makes it impossible for the player to win
'''

import json
import random

#Loads player scores from json file

def player_scores():

    with open("scores.json","r") as f:
        scores = json.load(f)

    with open("wins.json","r") as f:
        wins = json.load(f)

    with open("draws.json","r") as f:
        draws = json.load(f)
        
    with open("losses.json","r") as f:
        losses = json.load(f)
        

    return scores, wins, draws, losses

#Asks player which mode they would like to play - Human or Play against computer

def select_player_mode():
    player_mode = input("\nPlease select your game mode: Human - (H) Computer - (C): ").upper()
    while player_mode != "H" and player_mode != "C":
        print("The player mode you entered was invalid. Please enter: H or C")
        player_mode = input("\nPlease select your game mode: Human - (H) Computer - (C): ").upper()
    if player_mode == "C":
        print("You are playing against the computer")
    else:
        print("You are playing against a human player")
    return player_mode

#Prints the scoreboard to the screen   

def scoreboard(scores, wins, draws, losses):
    print("\n")
    print("\nScoreboard: ")
    print("\nPlayer:\t\t\tP:  W:  D:  L:")

    for player in scores:
        print(player," "*(22-len(player)),scores[player]," ",wins[player]," ",draws[player]," ",losses[player])
     
#Initialise the board

def board_setup():
    
    game = [['1', '1', '1'],
            ['1', '1', '1'],
            ['1', '1', '1']]

    return game

#Welcome players to the game

def welcome():

    print("\nWelcome to the Tic Tac Toe Game")

#Get player names and update player score to zero if new player

def get_players(scores, wins, draws, losses, player_mode):
    if player_mode == "H":
        print("\n")
        player1 = input("Player 1 please enter your name: ").strip().upper()
        while player1 == "":
            print("You did not enter a player name. Please re-enter")
            player1 = input("\nPlayer 1 please enter your name: ").strip().upper()
        player2 = input("Player 2 please enter your name: ").strip().upper()
        while player2 == "" or player2 == player1:
            if player2 == "":
                print("You did not enter a player name. Please re-enter")
            else:
                print("You have entered the same name as player 1. Please enter a different name")
            player2 = input("\nPlayer 2 please enter your name: ").strip().upper()
    else:
        player_choice = random.randint(1,2)
        if player_choice == 1:
            player1 = "COMPUTER"
            player2 = input("\nHuman Player please enter your name: ").strip().upper()
            while player2 == "" or player2 == "Computer":
                if player2 == "":
                    print("You did not enter a player name. Please re-enter")
                else:
                    print("You cannot use the name Computer. Please enter a different name")
                player2 = input("\nHuman Player please enter your name: ").strip().upper()
        else:
            player1 = input("\nHuman Player please enter your name: ").strip().upper()
            while player1 == "" or player1 == "COMPUTER":
                if player1 == "":
                    print("You did not enter a player name. Please re-enter")
                else:
                    print("You cannot use the name Computer. Please enter a different name")
                player1 = input("\nHuman Player please enter your name: ").strip().upper()
            player2 = "COMPUTER"
    if player1 not in scores:
        scores[player1] = 0
        wins[player1] = 0
        draws[player1] = 0
        losses[player1] = 0
    if player2 not in scores:
        scores[player2] = 0
        wins[player2] = 0
        draws[player2] = 0
        losses[player2] = 0
    

    return(player1, player2, scores, wins, draws, losses)

#Determines the players turn
#and sets move and player name

def player_turn(turn, player1, player2):
    
    if turn == 1:
        turn = 0
        player = player1
        move = "X"
    else:
        turn = 1
        player = player2
        move = "O"

    return(turn, player, move)

#Ask player for move
#Play against computer - easy mode - Generates random position:
#Play against computer - hard mode - runs through algorithm which makes it impossible to win

def ask_player_for_move(game, player, move, move_valid, player_mode, difficulty, computer_made_middle_move):
    
    if player != "COMPUTER":
        print("\n")
        print(player, "it is your turn")
        p_move = input("Please enter your move in the format (row,col) ")
        while len(p_move) != 3 or (p_move[0] != '1' and p_move[0] != '2' and p_move[0] != '3') or (p_move[1] != ",") or (p_move[2] != '1' and p_move[2] != '2' and p_move[2] != '3'):
            print("\nYou have entered a move that is not valid. Please re-enter")
            p_move = input("Please enter your move in the format (row,col) ").strip()
        pos = p_move.split(",")
    else:
        if move_valid == True:
            print("\nThe computer will make a move")
        if difficulty == "E":
            pos = random.randint(1,3),random.randint(1,3)
        else:
            if move == "X" and game[0][0] == "1" and game[0][1] == "X" and game[0][2] == "X":
                pos = 1,1
            elif move == "O" and game[0][0] == "1" and game[0][1] == "O" and game[0][2] == "O":
                pos = 1,1
            elif move == "X" and game[0][0] == "1" and game[1][0] == "X" and game[2][0] == "X":
                pos = 1,1
            elif move == "O" and game[0][0] == "1" and game[1][0] == "O" and game[2][0] == "O":
                pos = 1,1  
            elif move == "X" and game[0][0] == "1" and game[1][1] == "X" and game[2][2] == "X":
                pos = 1,1
            elif move == "O" and game[0][0] == "1" and game[1][1] == "O" and game[2][2] == "O":
                pos = 1,1
            elif move == "X" and game[0][1] == "1" and game[0][0] == "X" and game[0][2] == "X":
                pos = 1,2
            elif move == "O" and game[0][1] == "1" and game[0][0] == "O" and game[0][2] == "O":
                pos = 1,2
            elif move == "X" and game[0][1] == "1" and game[1][1] == "X" and game[2][1] == "X":
                pos = 1,2
            elif move == "O" and game[0][1] == "1" and game[1][1] == "O" and game[2][1] == "O":
                pos = 1,2
            elif move == "X" and game[0][2] == "1" and game[0][0] == "X" and game[0][1] == "X":
                pos = 1,3
            elif move == "O" and game[0][2] == "1" and game[0][0] == "O" and game[0][1] == "O":
                pos = 1,3
            elif move == "X" and game[0][2] == "1" and game[1][2] == "X" and game[2][2] == "X":
                pos = 1,3
            elif move == "O" and game[0][2] == "1" and game[1][2] == "O" and game[2][2] == "O":
                pos = 1,3
            elif move == "X" and game[0][2] == "1" and game[1][1] == "X" and game[2][0] == "X":
                pos = 1,3
            elif move == "O" and game[0][2] == "1" and game[1][1] == "O" and game[2][0] == "O":
                pos = 1,3
            elif move == "X" and game[1][0] == "1" and game[1][1] == "X" and game[1][2] == "X":
                pos = 2,1
            elif move == "O" and game[1][0] == "1" and game[1][1] == "O" and game[1][2] == "O":
                pos = 2,1
            elif move == "X" and game[1][0] == "1" and game[0][0] == "X" and game[2][0] == "X":
                pos = 2,1
            elif move == "O" and game[1][0] == "1" and game[0][0] == "O" and game[2][0] == "O":
                pos = 2,1
            elif move == "X" and game[1][1] == "1" and game[1][0] == "X" and game[1][2] == "X":
                pos = 2,2
            elif move == "O" and game[1][1] == "1" and game[1][0] == "O" and game[1][2] == "O":
                pos = 2,2
            elif move == "X" and game[1][1] == "1" and game[0][1] == "X" and game[2][1] == "X":
                pos = 2,2
            elif move == "O" and game[1][1] == "1" and game[0][1] == "O" and game[2][1] == "O":
                pos = 2,2
            elif move == "X" and game[1][1] == "1" and game[0][0] == "X" and game[2][2] == "X":
                pos = 2,2
            elif move == "O" and game[1][1] == "1" and game[0][0] == "O" and game[2][2] == "O":
                pos = 2,2
            elif move == "X" and game[1][1] == "1" and game[0][2] == "X" and game[2][0] == "X":
                pos = 2,2
            elif move == "O" and game[1][1] == "1" and game[0][2] == "O" and game[2][0] == "O":
                pos = 2,2
            elif move == "X" and game[1][2] == "1" and game[1][0] == "X" and game[1][1] == "X":
                pos = 2,3
            elif move == "O" and game[1][2] == "1" and game[1][0] == "O" and game[1][1] == "O":
                pos = 2,3
            elif move == "X" and game[1][2] == "1" and game[0][2] == "X" and game[2][2] == "X":
                pos = 2,3
            elif move == "O" and game[1][2] == "1" and game[0][2] == "O" and game[2][2] == "O":
                pos = 2,3
            elif move == "X" and game[2][0] == "1" and game[0][0] == "X" and game[1][0] == "X":
                pos = 3,1
            elif move == "O" and game[2][0] == "1" and game[0][0] == "O" and game[1][0] == "O":
                pos = 3,1
            elif move == "X" and game[2][0] == "1" and game[2][1] == "X" and game[2][2] == "X":
                pos = 3,1
            elif move == "O" and game[2][0] == "1" and game[2][1] == "O" and game[2][2] == "O":
                pos = 3,1
            elif move == "X" and game[2][0] == "1" and game[1][1] == "X" and game[0][2] == "X":
                pos = 3,1
            elif move == "O" and game[2][0] == "1" and game[1][1] == "O" and game[0][2] == "O":
                pos = 3,1  
            elif move == "X" and game[2][1] == "1" and game[2][0] == "X" and game[2][2] == "X":
                pos = 3,2
            elif move == "O" and game[2][1] == "1" and game[2][0] == "O" and game[2][2] == "O":
                pos = 3,2
            elif move == "X" and game[2][1] == "1" and game[0][1] == "X" and game[1][1] == "X":
                pos = 3,2
            elif move == "O" and game[2][1] == "1" and game[0][1] == "O" and game[1][1] == "O":
                pos = 3,2
            elif move == "X" and game[2][2] == "1" and game[2][0] == "X" and game[2][1] == "X":
                pos = 3,3
            elif move == "O" and game[2][2] == "1" and game[2][0] == "O" and game[2][1] == "O":
                pos = 3,3
            elif move == "X" and game[2][2] == "1" and game[0][2] == "X" and game[1][2] == "X":
                pos = 3,3
            elif move == "O" and game[2][2] == "1" and game[0][2] == "O" and game[1][2] == "O":
                pos = 3,3
            elif move == "X" and game[2][2] == "1" and game[0][0] == "X" and game[1][1] == "X":
                pos = 3,3
            elif move == "O" and game[2][2] == "1" and game[0][0] == "O" and game[1][1] == "O":
                pos = 3,3
            elif move == "O" and game[0][0] == "1" and game[0][1] == "X" and game[0][2] == "X":
                pos = 1,1
            elif move == "X" and game[0][0] == "1" and game[0][1] == "O" and game[0][2] == "O":
                pos = 1,1
            elif move == "O" and game[0][0] == "1" and game[1][0] == "X" and game[2][0] == "X":
                pos = 1,1
            elif move == "X" and game[0][0] == "1" and game[1][0] == "O" and game[2][0] == "O":
                pos = 1,1  
            elif move == "O" and game[0][0] == "1" and game[1][1] == "X" and game[2][2] == "X":
                pos = 1,1
            elif move == "X" and game[0][0] == "1" and game[1][1] == "O" and game[2][2] == "O":
                pos = 1,1
            elif move == "O" and game[0][1] == "1" and game[0][0] == "X" and game[0][2] == "X":
                pos = 1,2
            elif move == "X" and game[0][1] == "1" and game[0][0] == "O" and game[0][2] == "O":
                pos = 1,2
            elif move == "O" and game[0][1] == "1" and game[1][1] == "X" and game[2][1] == "X":
                pos = 1,2
            elif move == "X" and game[0][1] == "1" and game[1][1] == "O" and game[2][1] == "O":
                pos = 1,2
            elif move == "O" and game[0][2] == "1" and game[0][0] == "X" and game[0][1] == "X":
                pos = 1,3
            elif move == "X" and game[0][2] == "1" and game[0][0] == "O" and game[0][1] == "O":
                pos = 1,3
            elif move == "O" and game[0][2] == "1" and game[1][2] == "X" and game[2][2] == "X":
                pos = 1,3
            elif move == "X" and game[0][2] == "1" and game[1][2] == "O" and game[2][2] == "O":
                pos = 1,3
            elif move == "O" and game[0][2] == "1" and game[1][1] == "X" and game[2][0] == "X":
                pos = 1,3
            elif move == "X" and game[0][2] == "1" and game[1][1] == "O" and game[2][0] == "O":
                pos = 1,3
            elif move == "O" and game[1][0] == "1" and game[1][1] == "X" and game[1][2] == "X":
                pos = 2,1
            elif move == "X" and game[1][0] == "1" and game[1][1] == "O" and game[1][2] == "O":
                pos = 2,1
            elif move == "O" and game[1][0] == "1" and game[0][0] == "X" and game[2][0] == "X":
                pos = 2,1
            elif move == "X" and game[1][0] == "1" and game[0][0] == "O" and game[2][0] == "O":
                pos = 2,1
            elif move == "O" and game[1][1] == "1" and game[1][0] == "X" and game[1][2] == "X":
                pos = 2,2
            elif move == "X" and game[1][1] == "1" and game[1][0] == "O" and game[1][2] == "O":
                pos = 2,2
            elif move == "O" and game[1][1] == "1" and game[0][1] == "X" and game[2][1] == "X":
                pos = 2,2
            elif move == "X" and game[1][1] == "1" and game[0][1] == "O" and game[2][1] == "O":
                pos = 2,2
            elif move == "O" and game[1][1] == "1" and game[0][0] == "X" and game[2][2] == "X":
                pos = 2,2
            elif move == "X" and game[1][1] == "1" and game[0][0] == "O" and game[2][2] == "O":
                pos = 2,2
            elif move == "O" and game[1][1] == "1" and game[0][2] == "X" and game[2][0] == "X":
                pos = 2,2
            elif move == "X" and game[1][1] == "1" and game[0][2] == "O" and game[2][0] == "O":
                pos = 2,2
            elif move == "O" and game[1][2] == "1" and game[1][0] == "X" and game[1][1] == "X":
                pos = 2,3
            elif move == "X" and game[1][2] == "1" and game[1][0] == "O" and game[1][1] == "O":
                pos = 2,3
            elif move == "O" and game[1][2] == "1" and game[0][2] == "X" and game[2][2] == "X":
                pos = 2,3
            elif move == "X" and game[1][2] == "1" and game[0][2] == "O" and game[2][2] == "O":
                pos = 2,3
            elif move == "O" and game[2][0] == "1" and game[0][0] == "X" and game[1][0] == "X":
                pos = 3,1
            elif move == "X" and game[2][0] == "1" and game[0][0] == "O" and game[1][0] == "O":
                pos = 3,1
            elif move == "O" and game[2][0] == "1" and game[2][1] == "X" and game[2][2] == "X":
                pos = 3,1
            elif move == "X" and game[2][0] == "1" and game[2][1] == "O" and game[2][2] == "O":
                pos = 3,1
            elif move == "O" and game[2][0] == "1" and game[1][1] == "X" and game[0][2] == "X":
                pos = 3,1
            elif move == "X" and game[2][0] == "1" and game[1][1] == "O" and game[0][2] == "O":
                pos = 3,1  
            elif move == "O" and game[2][1] == "1" and game[2][0] == "X" and game[2][2] == "X":
                pos = 3,2
            elif move == "X" and game[2][1] == "1" and game[2][0] == "O" and game[2][2] == "O":
                pos = 3,2
            elif move == "O" and game[2][1] == "1" and game[0][1] == "X" and game[1][1] == "X":
                pos = 3,2
            elif move == "X" and game[2][1] == "1" and game[0][1] == "O" and game[1][1] == "O":
                pos = 3,2
            elif move == "O" and game[2][2] == "1" and game[2][0] == "X" and game[2][1] == "X":
                pos = 3,3
            elif move == "X" and game[2][2] == "1" and game[2][0] == "O" and game[2][1] == "O":
                pos = 3,3
            elif move == "O" and game[2][2] == "1" and game[0][2] == "X" and game[1][2] == "X":
                pos = 3,3
            elif move == "X" and game[2][2] == "1" and game[0][2] == "O" and game[1][2] == "O":
                pos = 3,3
            elif move == "O" and game[2][2] == "1" and game[0][0] == "X" and game[1][1] == "X":
                pos = 3,3
            elif move == "X" and game[2][2] == "1" and game[0][0] == "O" and game[1][1] == "O":
                pos = 3,3
            elif move == "X" and game[1][1] == "1":
                pos = 2,2
                computer_made_middle_move = True
            elif move == "O" and game[1][1] == "1":
                pos = 2,2
                computer_made_middle_move = True
            elif move == "X" and computer_made_middle_move == True and game[0][0] == "O" and game[2][1] == "1":
                pos = 3,2
            elif move == "X" and computer_made_middle_move == True and game[0][2] == "O" and game[2][1] == "1":
                pos = 3,2
            elif move == "O" and computer_made_middle_move == True and game[0][0] == "X" and game[2][1] == "1":
                pos = 3,2
            elif move == "O" and computer_made_middle_move == True and game[0][2] == "X" and game[2][1] == "1":
                pos = 3,2      
            elif move == "X" and computer_made_middle_move == True and game[0][1] == "1" and game[2][1] == "1":
                pos = 1,2
            elif move == "O" and computer_made_middle_move == True and game[0][1] == "1" and game[2][1] == "1":
                pos = 1,2
            elif move == "X" and computer_made_middle_move == True and game[2][1] == "1" and game[0][1] == "1":
                pos = 3,2
            elif move == "O" and computer_made_middle_move == True and game[2][1] == "1" and game[0][1] == "1":
                pos = 3,2
            #Blocks multiple wins lines from all angles 
            elif move == "O" and game[0][0] == "X" and game[2][1] == "X" and game[2][0] == "1":
                pos = 3,1
            elif move == "O" and game[0][2] == "X" and game[2][1] == "X" and game[2][2] == "1":
                pos = 3,3
            elif move == "O" and game[1][2] == "X" and game[2][1] == "X" and game[2][2] == "1":
                pos = 3,3
            elif game[0][0] == "1":
                pos = 1,1
            elif game[0][2] == "1":
                pos = 1,3
            elif game[2][0] == "1":
                pos = 3,1
            elif game[2][2] == "1":
                pos = 3,3
            elif game[1][1] == "1":
                pos = 2,2
            elif game[0][0] == "1" or game[0][1] == "1" or game[0][2] == "1" or game[1][0] == "1" or game[1][1] == "1" or game[1][2] == "1" or game[2][0] == "1" or game[2][1] == "1" or game[2][2] == "1":
                pos = random.randint(1,3), random.randint(1,3)
                    
    return pos, computer_made_middle_move

#Checks if move has been taken

def check_move_valid(game, pos, move_valid, player):

    if game[int(pos[0])-1][int(pos[1])-1] == "X" or game[int(pos[0])-1][int(pos[1])-1] == "O":
        if player != "COMPUTER":
            print("\nYou cannot make a move here")
        move_valid = False
    else:
        move_valid = True

    return move_valid

#Places move on the game board

def place_move(game, pos, move):
    game[int(pos[0])-1][int(pos[1])-1] = move

#Prints the game board to the screen

def print_board(game):
    print("\n")
    for x in range(0,3):
        print(game[x])

#Check Horizontal wins

def check_horizontal_wins(game, move, player, win, winner):

    for x in range(0,3):
        if game[x][0] == move and game[x][1] == move and game[x][2] == move:
            winner = player
            win = True
    return win, winner
 
#Check Vertical wins

def check_vertical_wins(game, move, player, win, winner):
    
    for x in range(0,3):
        if game[0][x] == move and game[1][x] == move and game [2][x] == move:
            winner = player
            win = True
    return win, winner
      
#Check Diagonal Left wins

def check_diagonal_left_wins(game, move, player, win, winner):

    if game[0][0] == move and game[1][1] == move and game[2][2] == move:
        winner = player
        win = True

    return win, winner

#Check Diagonal Right wins

def check_diagonal_right_wins(game, move, player, win, winner):
    if game[0][2] == move and game[1][1] == move and game[2][0] == move:
        winner = player
        win = True

    return win, winner


#Displays the winner on screen

def display_winner(win, winner):
    if win == True:
        if winner == "COMPUTER":
            print("\nThe computer has won!")
        else:
            print("\nCongratulations!", winner, "you have won")
    else:
        print("\nIt is a draw!")

#Checks if the board is full to determine if the game is a draw

def check_board_full(game, board_full):
    board_full = True
    for x in range(0,3):
        for y in range(0,3):
            if game[x][y] == "1":
                board_full = False
                break

    return board_full

#Aks player if they would like to play again

def play_again(gameplay):

    gameplay = input("\nWould you like to play again (Y/N)?: ").upper()
    while gameplay != "Y" and gameplay != "N":
        print("Your choice is invalid. Please enter Y or N")
        gameplay = input("\nWould you like to play again (Y/N)?: ").upper()
    return gameplay

#Updates the player scores

def update_player_scores(winner, player1, player2, scores, wins, draws, losses):

    if winner == player1:
        wins[player1] +=1
        scores[player1] +=1
        losses[player2] +=1
    elif winner == player2:
        wins[player2] +=1
        scores[player2] +=1
        losses[player1] +=1
    else:
        scores[player1] +=1
        scores[player2] +=1
        draws[player1] +=1
        draws[player2] +=1

    return scores, wins, draws, losses

#Saves scores in the game to json file

def save_scores(scores, wins, draws, losses):

    with open("scores.json", "w") as f:
        scores = json.dump(scores, f)
    f.close()
  
    with open("wins.json", "w") as f:
        wins = json.dump(wins, f)
    f.close()

    with open("draws.json", "w") as f:
        draws = json.dump(draws, f)
    f.close()

    with open("losses.json", "w") as f:
        losses = json.dump(losses, f)
    f.close()

#Asks player to select difficulty when playing against the computer
    
def select_difficulty():

    difficulty = input("\nPlease enter the level of difficulty you would like to play - (E)Easy or (H)Hard: ").upper()
    while difficulty != "E" and difficulty != "H":
        print("You have entered an invalid difficulty. Please enter E or H")
        difficulty = input("\nPlease enter the level of difficulty you would like to play - (E)Easy or (H)Hard: ").upper()
    if difficulty == "E":
        print("You are playing the easy mode")
    else:
        print("You are playing the hard mode")

    return difficulty
    
#The main function
               
def main():
    gameplay = "Y"
    difficulty = ""
    welcome()
    scores, wins, draws, losses = player_scores()
    player_mode = select_player_mode()
    if player_mode == "C":
        difficulty = select_difficulty()
    player1, player2, scores, wins, draws, losses = get_players(scores, wins, draws, losses, player_mode)
    while gameplay == "Y":
        winner = ""
        computer_made_middle_move = False
        turn = 1
        move_valid = True
        win = False
        board_full = False
        game = board_setup()
        scoreboard(scores, wins, draws, losses)
        print_board(game)
        while win == False and board_full == False:
            turn, player, move = player_turn(turn, player1, player2)
            pos, computer_made_middle_move = ask_player_for_move(game, player, move, move_valid, player_mode, difficulty, computer_made_middle_move)
            move_valid = check_move_valid(game, pos, move_valid, player)
            while move_valid == False:
                if player != "COMPUTER":
                    print_board(game)
                pos, computer_made_middle_move = ask_player_for_move(game, player, move, move_valid, player_mode, difficulty, computer_made_middle_move)
                move_valid = check_move_valid(game, pos, move_valid, player)
            place_move(game, pos, move)
            print_board(game)
            win, winner = check_horizontal_wins(game, move, player, win, winner)
            win, winner = check_vertical_wins(game, move, player, win, winner)
            win, winner = check_diagonal_left_wins(game, move, player, win, winner)
            win, winner = check_diagonal_right_wins(game, move, player, win, winner)
            board_full = check_board_full(game, board_full)
        display_winner(win, winner)
        scores, wins, draws, losses = update_player_scores(winner, player1, player2, scores, wins, draws, losses)
        save_scores(scores, wins, draws, losses)
        scoreboard(scores, wins, draws, losses)
        gameplay = play_again(gameplay)

main()
    

     
