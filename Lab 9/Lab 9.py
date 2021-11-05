#Nathan Gregorian Bailey
#Section 0003
#Program 9
#Created on November 2nd 2021 
#Due November 5th 2021
import csv
def month_from_number(num):
    months = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    if num in months.keys():
        return months[num]
    else:
        raise ValueError

def read_in_file(x):
    try:
        with open(x, 'r', encoding='utf-8') as f:
            reader_x = list(csv.reader(f))
            return reader_x
    except FileNotFoundError:
        raise FileNotFoundError



def date_type_mod(lsty):
    mod_listy = []
    for l in range(len(lsty)):
        date = lsty[l][0].split('/')

        for i in range(len(date)):
            date[i] = int(date[i])

        mod_listy.append((tuple(date), lsty[l][1], lsty[l][2]))
    return mod_listy


def create_reported_date_dict(lstz):
    reports_by_date = {}
    for l in lstz:
        if l[0] not in reports_by_date.keys():
            reports_by_date[l[0]] = 1
        else:
            reports_by_date[l[0]] += 1
    return reports_by_date


def create_reported_month_dict(lsta):
    reports_by_month = {}
    for l in range(len(lsta)):
        if lsta[l][0][0] not in reports_by_month.keys():
            reports_by_month[lsta[l][0][0]] = 1
        else:
            reports_by_month[lsta[l][0][0]] += 1
    return reports_by_month


def create_offense_dict(lstb):
    reports_by_offense = {}
    for l in range(len(lstb)):
        if lstb[l][1] not in reports_by_offense.keys():
            reports_by_offense[lstb[l][1]] = 1
        else:
            reports_by_offense[lstb[l][1]] += 1
    return reports_by_offense


def create_offense_by_zip(lstc):
    offense_by_zip = {}
    for l in range(len(lstc)):
        crime = lstc[l][1]
        zip = lstc[l][2]
        if crime not in offense_by_zip.keys():
            offense_by_zip[crime] = {lstc[l][2]: 1}
        elif zip not in offense_by_zip[crime]:
            offense_by_zip[crime][zip] = 1
        elif zip in offense_by_zip[crime]:
            offense_by_zip[crime][zip] += 1
        else:
            continue
    return offense_by_zip

def strip(lstx):
    stripped_listx = []
    for l in range(1, len(lstx)):
        stripped_listx.append((lstx[l][1], lstx[l][7], lstx[l][13]))
    return stripped_listx

checker = -1
while checker == -1:
    try:
        file_name = input('Enter the name of the crime data file: ').strip()
        critical_info = strip(read_in_file(file_name))
        date_modified_critical = date_type_mod(critical_info)
        sorted_dic = dict(sorted(create_reported_month_dict(date_modified_critical).items()))
        for key in sorted_dic.keys():
            if sorted_dic[key] == max(sorted_dic.values()):
                month_num = key
        sorted_offenses = dict(sorted(create_offense_dict(critical_info).items()))
        for key in sorted_offenses.keys():
            if sorted_offenses[key] == max(sorted_offenses.values()):
                frequent_offense = key
        print()
        print('The month with the highest # of crimes is', month_from_number(month_num), 'with',
                sorted_dic[month_num], 'offenses.')
        print('The offense with the highest # of crimes is', frequent_offense, 'with',
                sorted_offenses[frequent_offense], 'offenses.\n')
        checker = 0
    except FileNotFoundError:
        print('Could not find the file specified.', file_name, 'not found.')
checker2 = -1
while checker2 == -1:
    try:
        search_criteria = input('Enter an offense: ').strip().lower().capitalize()
        crime_dict = create_offense_by_zip(critical_info)[search_criteria]
        print()
        table_format = '{zipcode:<15}{count:>10}'
        if search_criteria in create_offense_by_zip(critical_info).keys():
            print(search_criteria, 'offenses by Zip Code')
            print(table_format.format(zipcode='Zip Code', count='# Offenses'))
            print('=' * 25)
            for sub_dic in crime_dict.keys():
                print(table_format.format(zipcode=sub_dic, count=crime_dict[sub_dic]))
            checker2 = 0
            print()
    except KeyError:
        print('Not a valid offense found, please try again.')
    except ValueError:
        print('ValueError: Month must be 1-12.')