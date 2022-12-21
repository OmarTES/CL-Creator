# Import date class from datetime module for Date inputs
from datetime import date




# Used by date_format() to recieve suffix of the day (ie. 1st, 2nd, 3rd, 4th)
def suffix(day):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

# formats the current date based on the input needed
def date_format(format, date):
    return date.strftime(format).replace('{suf}', str(date.day) + suffix(date.day))