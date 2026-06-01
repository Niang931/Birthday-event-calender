FILENAME = 'birthdays'
MONTH_INDEX = 0
DAY_INDEX = 1
NAME_INDEX = 2
CURRENT_YEAR = '2026'
import datetime


class BirthdayEvent:

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return f'{self.name} {self.date}'

    def to_dict(self):
        return {
            'name':self.name,
            'date':self.date
        }

class BirthdayCollection:

    def __init__(self):
        self.collection = []

    def load_birthdays(self):
        try:
            with open(FILENAME, 'r') as f:
                for line in f:
                    if line == '':
                        continue
                    date_item = line.split()[:2]
                    date_str = ' '.join(date_item) + ' ' + CURRENT_YEAR
                    date_obj = datetime.datetime.strptime(date_str, "%b %d %Y")
                    name = ' '.join(line.split()[2:])
                    birthday = BirthdayEvent(name, date_obj)
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








    


