########################################################################
##
## CS 101 Lab
## Program #8 (Lab Week 9)
## Jacob Ford
## jwfhmp@umkc.edu
##
########################################################################

from math import sqrt

def printmenu():
    print('\n    Grade Menu')
    print('1 - Add Test\n2 - Remove Test\n3 - Clear Tests\n4 - Add Assignment')
    print('5 - Remove Assignment\n6 - Clear Assignments\nD - Display Scores\nQ - Quit')

def add(addtuple):
    grade_type, type_list = addtuple
    try:
        new_score = float(input('Enter the new {} score 0-100 ==> '.format(grade_type)))
        if new_score < 0:
            print('{} score must be greater than 0'.format(grade_type))
        else:
            type_list.append(new_score)
    except:
        print('Input is not a valid float')

def remove(removetuple):
    grade_type, type_list = removetuple
    try:
        remove_score = float(input('Enter the {} score to remove 0-100 ==> '.format(grade_type)))
        try:
            type_list.remove(remove_score)
        except ValueError:
            print('Could not find score {} to remove'.format(remove_score))
    except ValueError:
        print('Input is not a valid float')


def clear(cleartuple):
    grade_type, type_list = cleartuple
    type_list.clear()
    print('{} scores have been cleared'.format(grade_type))

def calculatescores(grade_type,weight):
    values = []
    values.append(len(grade_type)) #Number of tests/assignments
    if values[0] != 0:
        values.append(min(grade_type)) #Lowest score
        values.append(max(grade_type)) #Highest score
        values.append((sum(grade_type)/len(grade_type))) #Average
        std = 0
        for i in grade_type:
            std += ((i - values[3])**2)
        values.append(sqrt(std/values[0])) #Standard deviation
        weight_value = (values[3]*weight) #Multiplies avg by grade weight
    else:
        values.extend(['n/a','n/a','n/a','n/a']) #Fills new list with 'n/a' if tests/assignments are empty
        weight_value = 0
    return values, weight_value

def displayscores(scorestuple):
    tests, assignments = scorestuple
    test_values,weight_value = calculatescores(tests,.6)
    assignment_values,weight_value2 = calculatescores(assignments,.4)
    print('Type',' '*6,'num    ','min    ','max    ','avg     ','std')
    print('='*48)
    printscores('Tests',test_values)
    printscores('Programs',assignment_values)
    print('\nThe weighted grade is: {:.2f}'.format(weight_value+weight_value2))

def printscores(type_text,print_values):
    if print_values[0] != 0:
        format_scores = '{:12}{:<8}{:<8.1f}{:<8.1f}{:<8.2f}{:>4.2f}'
    else:
        format_scores = '{:12}{:<8}{:<8}{:<8}{:<8}{:>4}'
    print(format_scores.format(type_text,print_values[0],print_values[1],print_values[2],print_values[3],print_values[4]))

tests = []
assignments = []
menu = {'1':(add, ('Test',tests)),'2':(remove, ('Test',tests)),'3':(clear, ('Test',tests)),'4':(add, ('Assignment',assignments)),
        '5':(remove, ('Assignment',assignments)),'6':(clear, ('Assignment',assignments)),'D':(displayscores,(tests, assignments))}
#Each key of menu dictionary corresponds with user input. Each value is a tuple containing both a function to be called and the arguments that will be passed to that function.

def main():
    while True:
        usr_input = ''
        printmenu()
        usr_input = input('\n==> ').upper()
        print()
        if usr_input in menu:
            menu[usr_input][0](menu[usr_input][1])
        elif usr_input == 'Q':
            break
        else:
            print('Invalid input. Please select a choice from the menu')

main()