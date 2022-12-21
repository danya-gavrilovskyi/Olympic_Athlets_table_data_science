import argparse

def task1(filename, country, year):
    head = None
    is_first_line = True
    with open(filename, 'r') as file:
        for line in file.readlines():
            data = line.strip().split('/t')
            if is_first_line:
                head = data
                is_first_line = False
                continue

            if country == data[head.index('NOC')] and year == data[head.index('Year')]:
                pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--medals', action='store_true', required=False)
    parser.add_argument('--total', action='store_true', required=False)
    parser.add_argument('--filename', required=True)

    args = parser.parse_args()
    
