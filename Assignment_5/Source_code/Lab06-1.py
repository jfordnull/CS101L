########################################################################
##
## CS 101 Lab
## Program #5 (Lab Week 6)
## Jacob Ford
## jwfhmp@umkc.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
''' Program starts by asking for input from user. User can enter library card or Enter to
    exit. If user enters a library card, a function is called which checks the following
    conditions: 1.) That the length of the input is 10 characters. 2.) That the first 5
    characters are letters A-Z. 3.) that the last 3 characters are digits 0-9. 4.) That the
    6th character is a digit 1, 2, or 3 - these correspond with schools. 5.) that the 7th
    character is a digit 1, 2, 3, or 4 - these correspond with grade levels. 6.) That the last
    character/check digit matches the value calculated by the check digit function. If the
    input passes all of these checks the program verifies that the card is valid and ouputs
    the school and grade of the cardholder. Otherwise, the program informs the user that the
    card is invalid and gives an error explaining why.'''
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


import string


def character_value(char : str) -> int:
    ''' Returns 0 for A, 1 for B, etc. '''
    return (ord(char) - 65)    

def get_check_digit(idnumber : str) -> int:
    ''' Returns the check digit for the name and sid. '''
    checkdigit = 0
    for index, value in enumerate(idnumber[0:5]):
        checkdigit += (character_value(value) * (index + 1))
    for index, value in enumerate(idnumber[5:9]):
        checkdigit += (int(value) * (index + 6))
    return checkdigit % 10

def is_valid(idnumber : str) -> tuple:
    ''' returns 2 values bool and a string with errors if bool is False '''   

def verify_check_digit(idnumber : str) -> tuple:
    ''' returns True if the check digit is valid, False if not '''
    if len(idnumber) != 10:
        return False, 'The length of the number given must be 10'
    for index, value in enumerate(idnumber[0:5]):
        if not value.isalpha():
            return False, 'The first 5 characters must be A-Z. The invalid character at index {} is {}'.format(index, value)
    for index, value in enumerate(idnumber[7:]):
        if not value.isdigit():
            return False, 'The last 3 characters must be 0-9. The invalid character at index {} is {}'.format((index + 7), value)
    if get_school(idnumber) == 'Invalid School':
        return False, 'The sixth character must be 1, 2, or 3' 
    elif get_grade(idnumber) == 'Invalid Grade':
        return False, 'The seventh character must be 1, 2, 3, or 4'
    elif get_check_digit(idnumber) != int(idnumber[9]):
        return False, 'Check digit {} does not match calculated value {}'.format(idnumber[9], get_check_digit(idnumber))
    else:
        return True, ''


def get_school(idnumber : str) -> str:
    ''' Returns the school the 5th index or 6th character is for. '''
    schools = {'1' : 'School of Computing and Engineering SCE', '2' : 'School of Law', '3' : 'College of Arts and Sciences'}
    if idnumber[5] in schools:
        return schools[idnumber[5]]
    else:
        return 'Invalid School'
  

def get_grade(idnumber : str) -> str:
    '''Returns the grade for index 6'''
    grades = {'1' : 'Freshman' , '2' : 'Sophomore', '3' : 'Junior', '4' : 'Senior'}
    if idnumber[6] in grades:
        return grades[idnumber[6]]
    else:
        return 'Invalid Grade'
   

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)
        