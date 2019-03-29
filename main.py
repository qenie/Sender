import re
import datetime

TEXT_MESSAGE = ''''Уважаемый(ая) {0}

               Позвольте от лица компании "Company" поздравить вас с Днем Рождения!
               Желаем вам всего хорошего в карьере, личной жизни и здоровья!

               Company — The Russian Software Engineering Expertise — Delivered Worldwide'''


def extract_emp_data():
    emp_names = list()
    emp_birth_dates = list()
    emp_birth_months = list()
    emp_emails = list()
    emp_numbers = 0
    with open('db.txt', 'r') as file:
        for line in file:
            emp_numbers += 1
            words = line.split()
            emp_names.append(words[0] + ' ' + words[1])
            emp_birth_dates.append(re.split(r'/', (words[2]))[0])
            emp_birth_months.append(re.split(r'/', (words[2]))[1])
            emp_emails.append(re.findall(r'\w+@\w+.\w+', line))
    return emp_names, emp_birth_dates, emp_birth_months, emp_emails, emp_numbers


def main():
    names, dates, months, emails, amount = extract_emp_data()
    current_date = datetime.datetime.now()
    day = current_date.day
    month = current_date.month

    for i in range(amount):
        if int(dates[i]) == day and int(months[i]) == month:
            print("The following message:\n" + TEXT_MESSAGE.format(names[i]) + "\nwill be sent to:" + str(emails[i]))


if __name__ == "__main__":
    main()
