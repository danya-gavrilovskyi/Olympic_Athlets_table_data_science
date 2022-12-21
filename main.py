import argparse
import sys
def head_taker(filename):
    with open(filename, 'r') as file:
        head = file.readline().strip().split('\t')
        return head
def first_task(file_name, medals, NOC, Year, output, total):
    with open(file_name, 'r') as file:
        countries_medals = {}
        count = 0
        medalist = []
        gold = 0
        silver = 0
        bronze = 0
        head = file.readline().strip().split('\t')
        right_year = True
        right_country = True
        for line in file.readlines():
            data = line.strip().split('\t')
            right_country = False if NOC != data[head.index('NOC')] else right_country
            right_year = False if Year != data[head.index('Year')] else right_year
            if NOC == data[head.index('NOC')] and Year == data[head.index('Year')] and data[head.index('Medal')] != 'NA':
                if count < 10:
                    count += 1
                    medalist.append(f'{data[head.index("Name")]} - {data[head.index("NOC")]} - {data[head.index("Medal")]}\n')
                if data[head.index('Medal')] == 'Gold' and NOC == data[head.index('NOC')]:
                    gold += 1
                else:
                    gold += 0
                if data[head.index('Medal')] == 'Silver' and NOC == data[head.index('NOC')]:
                    silver += 1
                else:
                    silver += 0
                if data[head.index('Medal')] == 'Bronze' and NOC == data[head.index('NOC')]:
                    bronze += 1
                else:
                    bronze += 0

        print('First 10:')
        medalist.append(f'Gold - {gold}\n')
        medalist.append(f'Silver - {silver}\n')
        medalist.append(f'Bronze - {bronze}\n')
        if right_country == False:
            print('Wrong country')
        if right_year == False:
            print('Wrong year')
        for i in medalist:
            if output != None:
                output_file = open(output, 'a')
                output_file.write(i)
                output_file.close()
            print(i, end='')
def task3(filename, *args):
    head = head_taker(filename)
    years_and_medals = {}
    for list in args:
        for country in list:
            years_and_medals.clear()
            with open(filename, 'r') as file:
                for line in file.readlines():
                    data = line.strip().split('\t')
                    if (data[head.index('Team')] == country or data[head.index('NOC')] == country) and data[head.index('Year')] not in years_and_medals and data[head.index('Medal')] != 'NA':
                        years_and_medals[data[head.index('Year')]] = 1
                    elif (data[head.index('Team')] == country or data[head.index('NOC')] == country) and data[head.index('Year')] in years_and_medals and data[head.index('Medal')] != 'NA':
                        years_and_medals[data[head.index('Year')]] += 1

            dict_values = [int(x) for x in years_and_medals.values()]
            dict_keys = [int(x) for x in years_and_medals.keys()]
            max_medals = max(dict_values)
            print(f"The most medals {country} earned in {dict_keys[dict_values.index(max_medals)]}'s year and the number was {max_medals}")
    return dict_values, dict_keys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('--medals', action='store_true', required=False)
    parser.add_argument('--total', action='store_true', required=False)
    parser.add_argument('--overall', nargs='*', required=False)
    parser.add_argument('--interactive', action='store_true', required=False)

    if sys.argv[2] == '--medals':
        parser.add_argument('country')
        parser.add_argument('year')
        parser.add_argument('--output')
        args = parser.parse_args()
        first_task(args.filename, args.country, args.year, args.output)
    elif sys.argv[2] == '--total':
        parser.add_argument('year')
        args = parser.parse_args()
        task2(args.filename, args.year)
    elif sys.argv[2] == '--overall':
        args = parser.parse_args()
        task3(args.filename, args.overall)
    elif sys.argv[2] == '--interactive':
        args = parser.parse_args()
        task4(args.filename)

if __name__ == '__main__':
    main()
