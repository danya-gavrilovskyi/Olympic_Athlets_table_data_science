import argparse

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
