def month_check(month):
    if month >=1 and month <=12:
        return True
    else:
        return False

def day_check(month,day):
    days_in_month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    month_valid = month_check(int(month))
    if month_valid:
        if 0 < day <= days_in_month(month):
            return True
        else:
            return False
    else:
        return False

def year_check(year):
    if year >= 1900 and year<= 2100:
        return True
    else:
        return False

def month_day_year(date):
    try:
        month,day,year = date.split("-")
        day_valid = day_check(int(month),int(day))
        month_valid = month_check(int(month))
        year_valid = year_check(int(year))
        if month_valid and day_valid and year_valid:
            print("{0} format is true".format(date))
        else:
            print("{0} format is wrong".format(date))
    except ValueError:
        print("Your input is Invalid")
        
        
