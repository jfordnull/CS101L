########################################################################
##
## CS 101 Lab
## Program #10
## Jacob Ford
## jwfhmp@umkc.edu
##
########################################################################

def read_usr_file(usr_file):
    with open(usr_file,'r') as usr_file:
        return usr_file.read().split()

def create_word_list(file_list):
    word_list = []
    for word in file_list:
        if word.isalnum():
            word_list.append(word.lower())
        else:
            new_str = ''
            for letter in word:
                if letter.isalnum():
                    new_str += letter
            word_list.append(new_str.lower())
    return word_list

def create_word_dict(word_list):
    word_dict = {}
    for word in word_list:
        if len(word) > 3:
            word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

def print_word_table(word_dict):
    line_format = '{:>2}{:>15}{:>15}'
    print('\nMost frequently used words:')
    print(line_format.format('#','Word','Freq.'))
    print('='*32)
    i = 1
    word_count, words_used_once = most_frequent_words(word_dict)
    while i <= 10 and i <= len(word_count):
            print(line_format.format(i,word_count[i-1][0],word_count[i-1][1]))
            i += 1
    print('\nThere are {} words that occur only once'.format(words_used_once))
    print('There are {} unique words in the document\n'.format(len(word_count)))

def most_frequent_words(word_dict):
    word_count = sorted(word_dict.items(),key=lambda elem:elem[1],reverse=True)
    words_used_once = 0
    for word in word_count:
        if word[1] == 1:
            words_used_once += 1
    return word_count, words_used_once

def main():
    while True:
        try:
            usr_file = input('\nEnter the name of the file to open: ')
            print_word_table(create_word_dict(create_word_list(read_usr_file(usr_file))))
            break
        except FileNotFoundError:
            print('\nCould not open file {}'.format(usr_file))
            print('Please try again')

main()