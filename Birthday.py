FILENAME = 'birthdays'
MONTH_INDEX = 0
DAY_INDEX = 1
NAME_INDEX = 2
CURRENT_YEAR = '2026'
import datetime


class BirthdayEvent:

    def __init__(self, name, date, end_date):
        self.name = name
        self.date = date
        self.end_date = end_date

    def __str__(self):
        return f'{self.name} {self.date}'


class BirthdayCollection:

    def __init__(self):
        self.collection = []

    def __iter__(self):
        for bd in self.collection:
            yield bd

    def load_birthdays(self):
        try:
            with open(FILENAME, 'r') as f:
                for line in f:
                    if line == '':
                        continue
                    date_item = line.split()[:2]
                    date_str = ' '.join(date_item) + ' ' + CURRENT_YEAR
                    date_obj = datetime.datetime.strptime(date_str, "%b %d %Y")
                    end_date = date_obj + datetime.timedelta(days=1)
                    name = ' '.join(line.split()[2:])
                    birthday = BirthdayEvent(name, date_obj, end_date)
                    self.collection.append(birthday)
        except FileNotFoundError:
            self.collection = []

    def list_birthdays(self):
        for birthday in self.collection:
            print(birthday)


if __name__ == '__main__':
    c = BirthdayCollection()
    c.load_birthdays()
    c.list_birthdays()








    


