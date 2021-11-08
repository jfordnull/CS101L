########################################################################
##
## CS 101 Lab
## Program #9 (Lab Week 10)
## Jacob Ford
## jwfhmp@umkc.edu
##
########################################################################

import csv

def month_from_number(month_num):
    months = {1:'January',2:'February',3:'March',4:'April',
              5:'May',6:'June',7:'July',8:'August',9:'September',
              10:'October',11:'November',12:'December'}
    if month_num not in months:
        raise ValueError('Month must be 1-12')
    return months[month_num]

def read_in_file(csv_string):
    csv_lists = []
    file_csv = csv.reader(open(csv_string, encoding='utf-8'))
    for line in file_csv:
        csv_lists.append(line)
    return csv_lists

def create_reported_date_dict(csv_lists):
    date_list = [i[1] for i in csv_lists if i != csv_lists[0]]
    crimes_on_date = {}
    for date in date_list:
        crimes_on_date[date] = crimes_on_date.get(date, 0) + 1
    return crimes_on_date

def create_reported_month_dict(csv_lists):
    month_list = [int(i[1][:2]) for i in csv_lists if i != csv_lists[0]]
    crimes_in_month = {}
    for month in month_list:
        crimes_in_month[month] = crimes_in_month.get(month, 0) + 1
    return crimes_in_month

def create_offense_dict(csv_lists):
    offense_list = [i[7] for i in csv_lists if i != csv_lists[0]]
    offense_dict = {}
    for offense in offense_list:
        offense_dict[offense] = offense_dict.get(offense, 0) + 1
    return offense_dict

def create_offense_by_zip_dict(csv_lists):
    offense_and_zip_list = [(i[7],i[13]) for i in csv_lists if i != csv_lists[0]]
    offense_by_zip_dict = {}
    for offense,zip in offense_and_zip_list:
        if offense not in offense_by_zip_dict:
            offense_by_zip_dict[offense] = {zip: 1}
        else:
            offense_by_zip_dict[offense][zip] = offense_by_zip_dict[offense].get(zip, 0) + 1
    return offense_by_zip_dict

def get_top_values(csv_dict):
    return [k for k,v in csv_dict.items() if v == max(list(csv_dict.values()))]

def print_values(offense_key,offense_by_zip):
    print()
    print('{} offenses by Zip Code'.format(offense_key))
    print('{:20}{:10}'.format('Zip Code','# Offenses'))
    print('='*30)
    for zip,offenses in offense_by_zip[offense_key].items():
        print('{:<20}{:>10}'.format(zip,offenses))

if __name__ == '__main__':
    while True:
        try:
            usr_file = input('Enter the name of the crime data file ==> ')
            csv_lists = read_in_file(usr_file)
            break
        except FileNotFoundError:
            print('Could not find the file specified. {} not found'.format(usr_file))
            continue
    
    print()
    months = create_reported_month_dict(csv_lists)
    offenses = create_offense_dict(csv_lists)
    print('The month with the highest # of crimes is {} with {} offenses'.format
    (month_from_number(get_top_values(months)[0]),months[get_top_values(months)[0]]))
    print('The offense with the highest # of crimes is {} with {} offenses'.format
    (get_top_values(offenses)[0],offenses[get_top_values(offenses)[0]]))

    offense_by_zip = create_offense_by_zip_dict(csv_lists)
    while True:
        offense_key = input('\nEnter an offense ==> ')
        if offense_key in offense_by_zip:
            break
        else:
            print('\nNot a valid offense. Please try again')
    print_values(offense_key,offense_by_zip)