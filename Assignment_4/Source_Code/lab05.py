########################################################################
##
## CS 101 Lab
## Program #4 (Lab Week 5)
## Jacob Ford
## jwfhmp@umkc.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      Program starts by asking for a bank value between 1-100 and then a wager. 
##      Program then spins three random #s between 1-10 and player receives/loses money
##      based on wager/matches in three random #s. Game continues until player bank 
##      runs out of funds.
## 
## ERROR HANDLING:
##      While loops keep program from proceeding unless player enters correct input
##      each time input is needed.
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random

def play_again() -> bool:
    while True:
        keep_playing = input('Do you want to play again? ==> ')
        if keep_playing.lower() == 'y':
            return True
        elif keep_playing.lower() == 'n':
            return False
        else:
            print('\nYou must enter Y/YES/N/NO to continue. Please try again')
            continue
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    while True:
        wager = int(input('How many chips do you want to wager? ==> '))
        if wager > 0 and wager <= bank:
            return wager
        elif wager <= 0:
            print('The wager amount must be greater than 0. Please enter again')
            continue
        elif wager > bank:
            print('The wager cannot be greater than how much you have')
            continue

def get_slot_results() -> tuple:
    return random.randint(1,10), random.randint(1,10), random.randint(1,10)

def get_matches(reela, reelb, reelc) -> int:
    match = 0
    if reela == reelb and reela == reelc:
        match = 3
    elif reela == reelc:
        match = 2
    elif reela == reelb:
        match = 2
    elif reelb == reelc:
        match = 2
    return match

def get_bank() -> int:
    while True:
        starting_chips = int(input('How many chips do you want to start with? ==> '))
        if starting_chips > 0 and starting_chips <= 100:
            return starting_chips
        elif starting_chips < 1:
            print('Too low a value. You can only choose 1-100 chips')
            continue
        elif starting_chips > 100:
            print('Too high a value. You can only choose 1-100 chips')
            continue

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return (wager * 10) - wager
    elif matches == 2:
        return (wager * 3) - wager
    else:
        return wager * -1 

if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        starting_bank = bank
        spin = 0
        mostchips = bank

        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            spin += 1
            if bank > mostchips:
                mostchips = bank
           
        print("You lost all", starting_bank, "in", spin, "spins")
        print("The most chips you had was", mostchips)
        playing = play_again()