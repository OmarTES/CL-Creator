from datetime import date
import pdfrw


def main():
    # Requests inputs that require manual incursion
    company = input("Enter company name: ")
    position = input("Enter position title: ")
    minor = input("Enter minor title: ")
    status = input("Enter a related status: ")
    subject = input("Enter a related subject: ")
    skill = input("Enter a related skill: ")
    workplace = input("Enter a related environment: ")

    # Read the PDF filed
    pdf = pdfrw.PdfReader('template.pdf')

    # Get the single page in the PDF
    page = pdf.getPage(0)

    # Modify the text on each page
    text = page.Contents.stream.decode('utf-8')
    text = insert_info(text, company, position, minor, status, subject, skill, workplace)
    page.Contents.stream = text.encode('utf-8')

    # Write the modified PDF to a new file
    pdfrw.PdfWriter().write('Cover Letter.pdf', pdf)

# Used by date_format() to receive suffix of the day (ie. 1st, 2nd, 3rd, 4th)
def suffix(day):
    return 'th' if 11<=day<=13 else {1:'st',2:'nd',3:'rd'}.get(day%10, 'th')

# Formats the current date based on the input needed
def date_format(format, date):
    return date.strftime(format).replace('{suf}', str(date.day) + suffix(date.day))

# Replaces temporary inputs with actual company information
def insert_info(text, company, position, minor, status, subject, skill, workplace):
    text = text.replace('[COMPANY]', company)
    text = text.replace('[POSITION]', position)
    text = text.replace('[MINOR]', minor)
    text = text.replace('[RELATED STATUS]', status)
    text = text.replace('[RELATED SUBJECT]', subject)
    text = text.replace('[RELATED SKILL]', skill)
    text = text.replace('[RELATED WORKPLACE]', workplace)
    return text

if __name__ == '__main__':
    main()