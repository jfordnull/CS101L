########################################################################
##
## CS 101 Lab
## Program #7 (Lab Week 8)
## Jacob Ford
## jwfhmp@umkc.edu
##
########################################################################

def get_min_mpg():
    while True:
        try:
            min_mpg = float(input('Enter minimum mpg ==> '))
            if min_mpg <= 0:
                print('Fuel economy must be greater than 0')
                continue
            elif min_mpg > 100:
                print('Fuel economy must be less than 100')
                continue
            else:
                print()
                return min_mpg
        except ValueError:
            print('You must enter a number for value economy')

def get_input_file():
    while True:
        try:
            prompt = input('Enter the name of the input vehicle file ==> ')
            input_file = open(prompt, 'r')
            print()
            return input_file
        except FileNotFoundError:
            print('Could not open file', prompt)
            continue

def get_output_file():
    while True:
        try:
            prompt = input('Enter the name of the file to output to ==> ')
            output_file = open(prompt,'w')
            print()
            return output_file
        except IOError:
            print('There is an IO Error',prompt)
            continue

def main():
    min_mpg = get_min_mpg()
    input_file = get_input_file()
    output_file = get_output_file()
    lines = input_file.readlines()
    lines.pop(0)
    for line in lines:
        line_elements = []
        line_elements = line.split('	')
        try:
            if float(line_elements[-3]) >= min_mpg:
                output_file.write('{} {}    {}  {:.3f}\n'.format(line_elements[0],line_elements[1],line_elements[2],float(line_elements[-3])))
                continue
            else:
                continue
        except ValueError:
            print('Could not convert {} for vehicle {} {} {}'.format(line_elements[-3],line_elements[0],line_elements[1],line_elements[2]))
            continue

main()