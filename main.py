import argparse

def head_taker(filename):
    with open(filename, 'r') as file:
        head = file.readline().strip().split('\t')
        return head

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
        task1(args.filename, args.country, args.year, args.output)
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
