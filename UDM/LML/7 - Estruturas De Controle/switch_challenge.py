import sys


def week_days():
    print('Welcome to the Week Day Finder')
    day = input('Please, enter the day you want to check: ').lower()
    WEEK_COLOR = {'RED': '\u001b[31m', 'GREEN': '\u001b[32m'}
    days = {
        '1' or 'sunday': 'Weekend Day',
        '2' or 'monday': 'Week Day',
        '3' or 'tuesday': 'Week Day',
        '4' or 'wednesday': 'Week Day',
        '5' or 'thursday': 'Week Day',
        '6' or 'friday': 'Week Day',
        '7' or 'saturday': 'Weekend Day'
    }

    try:
        if days[day] == 'Week Day':
            print(WEEK_COLOR['GREEN'], days[day])

        elif days[day] == 'Week Day':
            print(WEEK_COLOR['RED'], days[day])

    except KeyError:
        print('** Invalid Day **', file=sys.stderr)


def main():
    week_days()


main()
