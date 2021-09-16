'''
CS101 Lab
Program #3 (Lab Week 4)
Jacob Ford
jwfhmp@umkc.edu
'''

while True:
    print('Welcome to Flarsheim Guesser!\n')
    print('Please think of a number between and including 1 and 100.\n')

    #Get num % 3, check that input is valid
    while True:
        rem_by_three = int(input('What is the remainder when your number is divided by 3 ?\n'))
        if 0 <= rem_by_three <= 2:
            break
        elif rem_by_three < 0:
            print('The value entered must be greater than 0')
            continue
        else:
            print('The value entered must be less than 3')
            continue

    #Get num % 5
    rem_by_five = int(input('What is the remainder when your number is divided by 5 ?\n'))

    #Get num % 7, check that != num % 5
    while True:
        rem_by_seven = int(input('What is the remainder when your number is divided by 7 ?\n'))
        if rem_by_seven != rem_by_five:
            break
        else:
            print('The remainder when divided by 7 should not be the same as the remainder when divided by 5')
            continue

    #Calculate number
    for number in range(1,101):
        if number % 3 == rem_by_three:
            if number % 5 == rem_by_five:
                if number % 7 == rem_by_seven:
                    print('Your number was',number)
                    print('How amazing is that?')
                    break
                else:
                    continue
            else:
                continue
        else:
            continue
    
    #Check if user wants to play again
    while True:
        playagain = input('Do you want to play again? y to continue, n to quit ==> ')
        if playagain == 'y':
            continuegame = True
            break
        elif playagain == 'n':
            continuegame = False
            break
        else:
            continue

    #Decide to loop game or break
    if continuegame:
        continue
    else:
        break
