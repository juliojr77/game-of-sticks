import os

def get_sticks_amt():

    while True:

        try:
            total_sticks_val = int(input("How many sticks are there on the table initially (10-100)?: "))

        except ValueError:
            print('\n')
            input("Invalid entry... Use only numbers!!")
            continue

        if total_sticks_val not in range(10,101):
            print('\n')
            input("Sorry, you need to enter a number between 10 and 100.")
            continue
        else:
            break
    return total_sticks_val

def get_player_amt(player1, player2, remain_sticks):

    while True:
        try:
            if player1:
                player_sticks_num = int(input("Player 1: How many sticks do you take (1-3)?: "))


            if player2:
                player_sticks_num = int(input("Player 2: How many sticks do you take (1-3)?: "))

        except ValueError:
            print('\n')
            input("Invalid entry... Use only numbers!!")
            continue

        if player_sticks_num not in range(1,4):
            print('\n')
            input("Sorry, you need to enter a number between 1 and 3.")
            continue
        elif remain_sticks == 1 and  player_sticks_num > 1:
            print('\n')
            input("Sorry, you need to enter a number of lesser amount.")
            continue

        elif remain_sticks <= player_sticks_num and remain_sticks != 1:
            print('\n')
            input("Sorry, you need to enter a number of lesser amount.")
            continue
        else:
            break

    return player_sticks_num


#-------------------------------------

def play_game(sticks_amt):

    done = False
    game_tot_sticks = sticks_amt
    player1_turn = True
    player2_turn = False

    while True:
        print(' ')
        print('There are {} sticks on the board'.format(game_tot_sticks))
        if player1_turn:

            player_amt = get_player_amt(player1_turn, player2_turn, game_tot_sticks)
            if (game_tot_sticks - player_amt) >= 1:
                game_tot_sticks -= player_amt

                player1_turn = False
                player2_turn = True
                continue
            else:
                print('------------>>>  You loose..!')
                done = True

        if player2_turn:

            player_amt = get_player_amt(player1_turn, player2_turn, game_tot_sticks)
            if (game_tot_sticks - player_amt) >= 1:
                game_tot_sticks -= player_amt

                player2_turn = False
                player1_turn = True
                continue

            else:
                print('\n\n')
                print('You loose..!')
                done = True

        if done:
            print("\n\n")
            play_again = input("Play again? Y/N..:").lower()
            if play_again == 'y':
                return True
            else:
                return False

#-----------------------------------------------------------

def main():

    while True:

        os.system('clear')
        print('\n')
        print('WELCOME TO THE STICKS GAME')
        print('\n\n')

        if play_game(get_sticks_amt()):
            continue

        else:
            print('\n\n')
            print("Bye... Have a nice day")
            print('\n\n')
            sys.exit()




if __name__ == '__main__':
    main()
