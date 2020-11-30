# leap_year_month_checker.py


def is_leap(year):
    ''' Check if the year is a leap one '''

    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
        '''Take a given year by use and month and return the amount of
        days contained in that particular month.'''
        
        # check if month and year entered are valid
        if year < 1:
            return "NaY"
        elif month > 11 or month < 0:
            return "NaM"
        
        
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap(year) and month == 1:
            return month_days[month] + 1
        else:
            return month_days[month]

year = 0
month = 0

try:
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
except:
    print("Invalid Request")

days = days_in_month(year, month)
print(days)
