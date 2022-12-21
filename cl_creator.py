from datetime import date
from fpdf import FPDF

# Requests inputs that require manual incursion
company = input("Enter company name: ")
position = input("Enter position title: ")
minor = input("Enter minor title: ")
status = input("Enter a related status: ")
subject = input("Enter a related subject: ")
skill = input("Enter a related skill: ")
workplace = input("Enter a related environment: ")

# Used by date_format() to receive suffix of the day (ie. 1st, 2nd, 3rd, 4th)
def suffix(day):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

# formats the current date based on the input needed
def date_format(format, date):
    return date.strftime(format).replace('{suf}', str(date.day) + suffix(date.day))